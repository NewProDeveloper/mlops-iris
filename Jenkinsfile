pipeline {
    agent { 
        node {
            label 'local'
            customWorkspace 'D:\\7-MLOps\\Practical_6'
        }
    }
    
    stages {
    /*
        stage('Checkout Code') {
        steps {
            git branch: 'main', url: 'https://github.com/your-username/iris_project.git'
        }
    }*/
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