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
    }

    post {
        always {
            cleanWs()
        }
    }
}
