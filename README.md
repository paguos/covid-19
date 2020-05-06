# Covid-Dash

A web application based on [Dash](https://github.com/plotly/dash) to show insights of the global pandemic covid-19.
Using on the data provided by the public API [covid19api.com](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest).

## Requirements

- [Docker](https://docs.docker.com/get-docker/)

To run it locally outside docker:

- [Python 3.8.2](https://www.python.org/downloads/)
- [Pipenv](https://github.com/pypa/pipenv) dependency manager

For deployment:

- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS IAM Authenticator](https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Development

### Local

Install the dependencies:

```sh
cd app
pipenv install --dev
```

Run the application:

```sh
pipenv run app.py
```

Open [localhost:8050](http://localhost:8050) on your web browser.

### Docker

Run the tests:

```sh
make tests
```

Run the development application:

```sh
make run
```

Or run the deployment version of the application:

```sh
make ENV=deployment run
```

Open [localhost:8050](http://localhost:8050) on your web browser.

## Deployment

1. Create a kubernetes cluster using AWS Cloud Formation:

```sh
make cnf/create
```

2. Configure `kubectl` with the created cluster:

```sh
make eks/config
```

3. Apply the kubernetes resources of the application:

```sh
make k8s/deploy
```
