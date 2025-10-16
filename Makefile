.PHONY: all
all: generate

.PHONY: generate
generate:
	@echo "==> $@"
	./scripts/generate

.PHONY: update-pomerium
update-pomerium:
	@echo "==> $@"
	git submodule update --remote deps/github.com/pomerium
