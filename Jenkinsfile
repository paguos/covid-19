pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker { image 'python:3.8.2' }
            }
            steps {
                dir("app") {
                    sh 'pip install pipenv'
                    sh 'pipenv install --system'
                    sh 'pipenv run flake8'
                }
            }
        }
    }
}