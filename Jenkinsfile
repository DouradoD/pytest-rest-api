pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "pytest-rest-api-docker-image" // Name of the Docker image
    }
    stages {
        stage('Build Project Image') {
            steps {
                script {
                    // Build the project Docker image
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm ${DOCKER_IMAGE}"
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