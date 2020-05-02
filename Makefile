####################################################################################################
# Variables
####################################################################################################
AWS_REGION=us-west-2
BRANCH=$(shell git rev-parse --abbrev-ref HEAD)
ENV=development
IMAGE=covid-dash
REPOSITORY=paguos
VERSION=v0.0.0

####################################################################################################
# Docker
####################################################################################################

build:
	docker build . --target $(IMAGE)-$(ENV) -t $(IMAGE):$(ENV)

deploy: build
ifeq ($(VERSION), v0.0.0)
	docker tag $(IMAGE):$(ENV) $(REPOSITORY)/$(IMAGE):$(BRANCH)
	docker push $(REPOSITORY)/$(IMAGE):$(BRANCH)
else
	docker tag $(IMAGE):$(ENV) $(REPOSITORY)/$(IMAGE):$(VERSION)
	docker push $(REPOSITORY)/$(IMAGE):$(VERSION)
endif

run: build
	docker run -p 8050:8050 $(IMAGE):$(ENV)

test:
	docker build . --target $(IMAGE)-development -t $(IMAGE):development
	docker run $(IMAGE):development flake8
	docker run $(IMAGE):development python -m pytest

####################################################################################################
# CloudFormation & K8S
####################################################################################################

cnf/create:
	./scripts/create_stack.sh

cnf/update:
	./scripts/update_stack.sh

eks/config:
	aws eks --region $(AWS_REGION) update-kubeconfig --name covid-dash

k8s/deploy:
	kubectl apply -f kubernetes/