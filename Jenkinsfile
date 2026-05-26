pipeline {
    agent {
        docker {
            image 'python:3.14.5-alpine3.23'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "pip install -r requirements.txt --user"
                }
            }
        }

        stage('Unit tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Integration tests') {
            steps {
                sh 'pytest test_integration.py'
            }
        }

    }
}
