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
                sh '''
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
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
