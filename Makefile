run:
	docker build . --target app  -t covid-dash
	docker run -p 8050:8050 covid-dash

test:
	docker build . --target test -t covid-dash:test
	docker run covid-dash:test flake8
	docker run covid-dash:test python -m pytest

cnf/create:
	./scripts/create_stack.sh

cnf/update:
	./scripts/update_stack.sh