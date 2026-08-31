pipeline {
    agent any

    stages {

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jenkins-demo .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d --name jenkins-demo-container -p 8000:8000 jenkins-demo'
            }
        }

        stage('Test Container') {
            steps {
                bat 'pytest test_container.py'
            }
        }
    }

    post {
        always {
            bat 'docker stop jenkins-demo-container || exit 0'
            bat 'docker rm jenkins-demo-container || exit 0'
        }
    }
}