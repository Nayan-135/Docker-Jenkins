pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                '''
            }
        }

        stage('Install Dependencies (pip)') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install pytest pytest-cov
                    pytest --cov=app --cov-report=xml tests/
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
