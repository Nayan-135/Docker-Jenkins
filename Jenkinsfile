pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Install Dependencies (pip)') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                    pip install pytest pytest-cov
                    pytest --cov=app --cov-report=xml tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def app = docker.build("my-flask-app")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    app.run('-p 5000:5000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
