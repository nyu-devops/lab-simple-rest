# Makefile targets for development an testing
# Use make help for more info

.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: all
all: help

##@ Development

.PHONY: venv
venv: ## Create a Python virtual environment
	$(info Creating Python 3 virtual environment...)
	pipenv shell

.PHONY: install
install: ## Install dependencies
	$(info Installing dependencies...)
	pipenv install --dev

.PHONY: lint
lint: ## Run the linter
	$(info Running linting...)
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
	pylint . --max-line-length=127

.PHONY: test
test: ## Run the unit tests
	$(info Running tests...)
	pytest --disable-warnings

##@ Runtime

.PHONY: run
run: ## Run the service
	$(info Starting service...)
	flask run