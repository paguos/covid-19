pipeline {
    agent any

    environment {
        IMAGE_NAME = "paguos/covid-dash"
        SHORT_GIT_HASH = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
        VERSION = sh(script: "./scripts/semtag getcurrent", returnStdout: true).trim()
    }

    stages {
        stage("Lint Docker Image"){
            steps{
                sh "hadolint Dockerfile"
            }
        }
        stage ("Build Test Image"){
            steps {
                sh "docker build . --target covid-dash-development  -t covid-dash:development"
            }
        }
        stage('Tests') {
            parallel {
                stage('Lint') {
                    steps{
                        sh "docker run covid-dash:development flake8"
                    }
                }

                stage('Unit') {
                    steps{
                        sh "docker run covid-dash:development python -m pytest"
                    }
                }
            }

        }
        stage('Build') {
            steps {
                sh "docker build . --target covid-dash-deployment  -t ${IMAGE_NAME}:${SHORT_GIT_HASH}"
            }
        }
        stage('Deploy') {
            when { tag "v*" }
            steps {
                withDockerRegistry( [credentialsId: "dockerhub", url: "https://index.docker.io/v1/"] ) {
                    sh "docker tag ${IMAGE_NAME}:${SHORT_GIT_HASH} ${IMAGE_NAME}:${VERSION}"
                    sh "docker push ${IMAGE_NAME}:${VERSION}"
                }
            }
        }
    }
}