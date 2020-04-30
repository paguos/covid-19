aws_region=us-west-2
branch=$(shell git rev-parse --abbrev-ref HEAD)
image=covid-dash
docker_repository=paguos

deploy:
	docker build . --target $(image)-app -t $(docker_repository)/$(image):$(branch)
	docker push $(docker_repository)/$(image):$(branch)

run:
	docker build . --target $(image)-development  -t $(image):development
	docker run -p 8050:8050 $(image):development

test:
	docker build . --target $(image)-development -t $(image):development
	docker run $(image):test flake8
	docker run $(image):test python -m pytest

cnf/create:
	./scripts/create_stack.sh

cnf/update:
	./scripts/update_stack.sh

eks/config:
	aws eks --region $(aws_region) update-kubeconfig --name covid-dash

k8s/deploy:
	kubectl apply -f kubernetes/