pipeline {
    agent {
        docker {
            image 'python:3.14.5-alpine3.23'
        }
    }

    stages {

         stage('Initialize') {
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
