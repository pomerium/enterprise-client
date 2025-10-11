.PHONY: all
all: generate

.PHONY: generate
generate:
	@echo "==> $@"
	./scripts/generate
