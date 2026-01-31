pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
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
