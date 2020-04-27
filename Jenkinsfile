pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh "docker build . --target test  -t app:test"
                sh "docker run app:test flake8"
                sh "docker run app:test python -m pytest"
            }
        }
        stage('Deploy') {
            steps {
                withDockerRegistry( [credentialsId: "dockerhub", url: "https://index.docker.io/v1/"] ) {
                    sh "docker build . --target app  -t paguos/covid-dash:${BRANCH_NAME}-${BUILD_NUMBER}"
                    sh "docker push paguos/covid-dash:${BRANCH_NAME}-${BUILD_NUMBER}"
                }
            }
        }
    }
}