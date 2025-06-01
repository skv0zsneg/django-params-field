SHELL:=/usr/bin/env bash

.PHONY: unit
unit:
	poetry run pytest

.PHONY: typing
typing:
	poetry run mypy src

.PHONY: test
test: unit typing