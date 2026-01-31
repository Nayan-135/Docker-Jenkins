pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use 'bat' for Windows Command Prompt
                bat 'pip install -r requirements.txt'
            }
        }

      stage('Run Tests & Coverage') {
        steps {
            // Using 'python -m' solves most ModuleNotFound issues
            bat 'python -m pytest --cov=app --cov-report=xml tests/'
        }
    }

    }

    post {
        always {
            // Clean up the workspace after completion
            cleanWs()
        }
    }
}
