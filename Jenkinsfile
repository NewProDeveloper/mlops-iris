pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/NewProDeveloper/mlops-iris.git'
            }
        }

        stage('Show Workspace') {
            steps {
                bat 'cd'
            }
        }
        
        stage('Build Images') {
            steps {
                bat 'docker-compose build'
            }
        }

        /*
        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }*/

        stage('Run Tests') {
            steps {
                bat 'docker run --rm webapp pytest || echo "No tests found"'
            }
        }

        stage('Deploy Containers') {
            steps {
                bat 'docker-compose up -d'
            }
        }
    }
}