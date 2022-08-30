#!/bin/bash
set -euo pipefail

_tag="${1?"tag is required"}"

_script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
_temp_dir="$(mktemp -d)"
trap "exit 1" HUP INT PIPE QUIT TERM
trap 'rm -rf $_temp_dir' EXIT

# update protobuf definitions
git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "$_tag" \
    git@github.com:pomerium/pomerium-console \
    "$_temp_dir/pomerium-console"
(cd "$_temp_dir/pomerium-console" && git sparse-checkout set pkg/pb scripts)
rsync --archive --delete \
    --include='*/' --include="*.pb.go" --exclude="*" \
    "$_temp_dir/pomerium-console/pkg/pb/" \
    "$_script_dir/../go/pb/"
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/pomerium-console/pkg/pb/" \
    "$_script_dir/../proto/pomerium-console/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "$_tag" \
    git@github.com:pomerium/pomerium \
    "$_temp_dir/pomerium"
(cd "$_temp_dir/pomerium" && git sparse-checkout set pkg/grpc)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/pomerium/pkg/grpc/" \
    "$_script_dir/../proto/pomerium/"
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/pomerium/pkg/grpc/" \
    "$_script_dir/../proto/github.com/pomerium/pomerium/pkg/grpc/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "main" \
    git@github.com:cncf/xds \
    "$_temp_dir/xds"
(cd "$_temp_dir/xds" && git sparse-checkout set xds)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/xds/xds/" \
    "$_script_dir/../proto/xds/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "main" \
    git@github.com:cncf/udpa \
    "$_temp_dir/udpa"
(cd "$_temp_dir/udpa" && git sparse-checkout set udpa)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/udpa/udpa/" \
    "$_script_dir/../proto/udpa/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "main" \
    git@github.com:envoyproxy/data-plane-api \
    "$_temp_dir/data-plane-api"
(cd "$_temp_dir/data-plane-api" && git sparse-checkout set envoy)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/data-plane-api/envoy/" \
    "$_script_dir/../proto/envoy/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "master" \
    git@github.com:googleapis/googleapis \
    "$_temp_dir/googleapis"
(cd "$_temp_dir/googleapis" && git sparse-checkout set google)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/googleapis/google/" \
    "$_script_dir/../proto/google/"

git clone \
    --depth 1 \
    --filter=blob:none \
    --sparse \
    --branch "v0.6.7" \
    git@github.com:envoyproxy/protoc-gen-validate \
    "$_temp_dir/protoc-gen-validate"
(cd "$_temp_dir/protoc-gen-validate" && git sparse-checkout set validate)
rsync --archive --delete \
    --include='*/' --include="*.proto" --exclude="*" \
    "$_temp_dir/protoc-gen-validate/validate/" \
    "$_script_dir/../proto/validate/"

_deps=()
while read -r _proto; do
    _deps+=("$_proto")
done <"$_temp_dir/pomerium-console/scripts/proto-dependencies.txt"

# pip install grpcio grpcio-tools mypy-protobuf
python -m grpc_tools.protoc \
    --python_out=python/pb \
    --mypy_out=python/pb \
    -I "proto" \
    -I "proto/pomerium" \
    "${_deps[@]}"

(
    cd "proto/pomerium-console"
    python -m grpc_tools.protoc \
        --python_out="../../python/pb/pomerium/pb" \
        --mypy_out="../../python/pb/pomerium/pb" \
        --grpc_python_out="../../python/pb/pomerium/pb" \
        --mypy_grpc_out="../../python/pb/pomerium/pb" \
        -I ".." \
        -I "../pomerium" \
        -I "." \
        ./*.proto
)

find python/pb/ -type d -exec touch {}/__init__.py \;
