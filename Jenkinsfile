pipeline {
    agent any
    stages {
        stage('Build Project Image') {
            steps {
                script {
                    sh 'docker build -t pytest-restapi .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                        sh 'pytest -s -v --log-level=info --tb=auto --html=reports/report.html --self-contained-html'
                }
            }
        }
        stage('Archive Test Results') {
            steps {
                // Archive the test report
                archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            // Clean up Docker images
            script {
                sh "docker rmi ${env.DOCKER_IMAGE} || true"
            }
        }
    }
}