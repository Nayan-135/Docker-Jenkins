pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                // Pull code from repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Linux shell command
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                // Run pytest with coverage
                sh '''
                    python3 -m pytest --cov=app --cov-report=xml tests/
                '''
            }
        }
    }

    post {
        always {
            // Clean workspace after pipeline finishes
            cleanWs()
        }
    }
}
