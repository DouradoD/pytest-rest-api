pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "pytest-rest-api"
    }
    agent none // No global agent; define agents at the stage level
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Tests') {
        stage('Example') {
            agent any // Runs on any available agent
            steps {
                script {
                    // Run the Docker container and execute tests
                    docker.image("${env.DOCKER_IMAGE}").inside {
                        // Run pytest inside the container
                        sh 'pytest -s -v --log-level=info --tb=auto --html=reports/report.html --self-contained-html'
                    }
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
                echo 'Running on any agent'
            }
        }
    }
}
