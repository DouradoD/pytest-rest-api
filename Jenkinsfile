pipeline {
    agent any

    environment {
        // Set Python version (adjust as needed)
        PYTHON = 'python3.8'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the repository
                checkout scm
            }
        }

        stage('Set up Python environment') {
            steps {
                script {
                    // Ensure Python is installed
                    sh "${PYTHON} --version"

                    // Install virtualenv (if not already installed)
                    sh "${PYTHON} -m pip install --upgrade pip"
                    sh "${PYTHON} -m pip install virtualenv"

                    // Create and activate a virtual environment
                    sh "${PYTHON} -m virtualenv venv"
                    sh "source venv/bin/activate"
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Install project dependencies
                    sh "pip install -r requirements.txt"
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Run tests in parallel and generate an HTML report
                    sh "pytest -n 5 --html=report.html"
                }
            }
        }

        stage('Archive test report') {
            steps {
                // Archive the HTML report for later viewing
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment
            sh "rm -rf venv"
        }

        success {
            // Notify on success (optional)
            echo 'Tests executed successfully!'
        }

        failure {
            // Notify on failure (optional)
            echo 'Tests failed!'
        }
    }
}