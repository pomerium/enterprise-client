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
all: clean gen docs

.PHONY: clean
clean: clean-python clean-go

.PHONY: clean-python
clean-python:
	@echo "==> $@"
	$(RM) -r $(PREFIX)/python/pb

# requires: pip install grpcio grpcio-tools mypy-protobuf 
.PHONY: gen-python
gen-python:
	@echo "==> $@"
	@mkdir -p $(PREFIX)/python/pb $(PREFIX)/python/pb/pomerium/pb
	$(PYTHON) -m grpc_tools.protoc $(INCLUDES) --experimental_allow_proto3_optional --python_out=python/pb --mypy_out=python/pb $(DEPS_PROTOS)
	$(PYTHON) -m grpc_tools.protoc $(INCLUDES) --experimental_allow_proto3_optional --python_out=python/pb/pomerium/pb --mypy_out=python/pb/pomerium/pb --grpc_python_out=python/pb/pomerium/pb --mypy_grpc_out=python/pb/pomerium/pb $(PROTOS)
	# marking all directories as modules
	@find $(PREFIX)/python/pb/{pomerium/pb,envoy,validate,xds} -type d -exec touch {}/__init__.py \;
	# converting python to python3
	@2to3 -w -n $(PREFIX)/python/pb

.PHONY: pkg-python
pkg-python:
	@echo "==> $@"
	$(PYTHON) -m build $(PREFIX)/python

.PHONY: clean-go
clean-go:
	@echo "==> $@"
	$(RM) -r $(PREFIX)/go/pb

.PHONY: gen-go
gen-go:
	@echo "==> $@"
	@mkdir -p $(PREFIX)/go/pb
	protoc $(INCLUDES) --experimental_allow_proto3_optional --go_opt="$(GO_ENVOY_PATHS)" --go_out="plugins=grpc,paths=source_relative:go/pb" $(PROTOS)

.PHONY: gen
gen: gen-python gen-go docs

.PHONY: pkg
pkg: pkg-python

.PHONY: docs
docs:
	protoc --doc_out=./ --doc_opt=.template.mustache,API.md \
		--experimental_allow_proto3_optional=true \
		$(INCLUDES) \
		$(PROTOS)
