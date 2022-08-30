PREFIX?=$(shell pwd)
INCLUDES=-I proto/protoc-gen-validate -I proto/data-plane-api -I proto/pomerium -I proto/googleapis -I proto/xds
DEPS_PROTOS=proto/data-plane-api/envoy/config/core/v3/*.proto \
    proto/data-plane-api/envoy/config/cluster/v3/*.proto \
    $(shell find proto/data-plane-api/envoy/config/route -type f -name '*.proto') \
    $(shell find proto/data-plane-api/envoy/config/endpoint -type f -name '*.proto') \
    $(shell find proto/data-plane-api/envoy/annotations -type f -name '*.proto') \
    $(shell find proto/data-plane-api/envoy/type -type f -name '*.proto') \
 	proto/protoc-gen-validate/validate/*.proto \
	$(shell find proto/xds/xds -type f -name '*.proto')

GO_ENVOY_PATHS=Menvoy/config/route/v3/route_components.proto=github.com/envoyproxy/go-control-plane/envoy/config/route/v3,Menvoy/config/cluster/v3/cluster.proto=github.com/envoyproxy/go-control-plane/envoy/config/cluster/v3

PROTOS=proto/pomerium/*.proto

PYTHON:=python3

.PHONY: all
all: gen docs

.PHONY: pkg-python
pkg-python:
	@echo "==> $@"
	$(PYTHON) -m build $(PREFIX)/python

.PHONY: gen
gen: docs

.PHONY: pkg
pkg: pkg-python

.PHONY: docs
docs:
	protoc --doc_out=./ --doc_opt=.template.mustache,API.md \
		--experimental_allow_proto3_optional=true \
		$(INCLUDES) \
		$(PROTOS)
