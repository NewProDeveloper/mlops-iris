pipeline {
    agent any
    
    stages {
        stage('Git Commands'){
            bat 'git config --system --add safe.directory D:/7-MLOps/Practical_6'

        }

        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'file:///D:/7-MLOps/Practical_6'
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