.PHONY: setup run build preview lint test clean

setup:
	npm install

run:
	npm run dev

build:
	npm run build

preview:
	npm run preview

lint:
	npm run lint

test:
	npm test

clean:
	rm -rf dist
