pipeline {
    agent {
        docker {
            image 'python:3.14.5-alpine3.23'
        }
    }

    environment {
        HOME = "/tmp"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Unit tests') {
            steps {
                sh 'python3 -m pytest test_app.py'
            }
        }

        stage('Integration tests') {
            steps {
                sh 'python3 -m pytest test_integration.py'
            }
        }
    }
}
