.PHONY: setup run preview build lint test

PORT ?= 8000

setup:
	python3 --version

run:
	python3 -m http.server $(PORT) --bind 127.0.0.1 --directory site

preview: run

build: test

lint:
	python3 scripts/validate_site.py

test:
	python3 scripts/validate_site.py
