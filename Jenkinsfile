pipeline {
    agent { label 'master' }
    environment {
        // Set the required Python version
        PYTHON_VERSION = '3.10.5'
    }
    stages {
        stage('Check pyenv Installation') {
            steps {
                script {
                    // Check if pyenv is installed
                    def pyenvInstalled = bat(script: 'command -v pyenv', returnStatus: true) == 0
                    if (!pyenvInstalled) {
                        echo 'pyenv is not installed. Installing pyenv...'
                        // Install pyenv-win using Chocolatey
                        bat '''
                        Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
                        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
                        '''
                    } else {
                        echo 'pyenv is already installed.'
                    }
                }
            }
        }
        stage('Check Python Installation') {
            steps {
                script {
                    // Check if the required Python version is installed
                    def pythonInstalled = bat(script: "pyenv versions | findstr ${env.PYTHON_VERSION}", returnStatus: true) == 0
                    if (!pythonInstalled) {
                        echo "Python ${env.PYTHON_VERSION} is not installed. Installing Python ${env.PYTHON_VERSION}..."
                        // Install the required Python version
                        bat """
                        pyenv install ${env.PYTHON_VERSION}
                        """
                    } else {
                        echo "Python ${env.PYTHON_VERSION} is already installed."
                    }
                }
            }
        }
        stage('Check virtualenv Installation') {
            steps {
                script {
                    // Check if virtualenv is installed
                    def virtualenvInstalled = bat(script: 'python -m virtualenv --version', returnStatus: true) == 0
                    if (!virtualenvInstalled) {
                        echo 'virtualenv is not installed. Installing virtualenv...'
                        // Install virtualenv using pip
                        bat """
                        python -m pip install virtualenv
                        """
                    } else {
                        echo 'virtualenv is already installed.'
                    }
                }
            }
        }
        stage('Check pip Installation') {
            steps {
                script {
                    // Check if pip is installed
                    def pipInstalled = bat(script: 'python -m pip --version', returnStatus: true) == 0
                    if (!pipInstalled) {
                        echo 'pip is not installed. Installing pip...'
                        // Install pip using ensurepip
                        bat """
                        python -m ensurepip --upgrade
                        """
                    } else {
                        echo 'pip is already installed.'
                    }
                }
            }
        }
        stage('Set up Python Environment') {
            steps {
                script {
                    // Set the Python version for the project
                    bat """
                    pyenv local ${env.PYTHON_VERSION}
                    python --version
                    """
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    def isWindows = isUnix() ? false : true
                    if (isWindows) {
                        // Windows-specific setup
                        bat """
                        choco install pyenv-win -y
                        pyenv install ${env.PYTHON_VERSION} --force
                        pyenv local ${env.PYTHON_VERSION}
                        python -m venv venv
                        venv\\Scripts\\pip install -r requirements.txt
                        """
                    } else {
                        // Linux-specific setup
                        sh """
                        curl https://pyenv.run | bash
                        export PYENV_ROOT="\$HOME/.pyenv"
                        export PATH="\$PYENV_ROOT/bin:\$PATH"
                        eval "\$(pyenv init -)"
                        pyenv install ${env.PYTHON_VERSION} --force
                        pyenv local ${env.PYTHON_VERSION}
                        python -m venv venv
                        venv/bin/pip install -r requirements.txt
                        """
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    def isWindows = isUnix() ? false : true
                    if (isWindows) {
                        bat 'venv\\Scripts\\pytest'
                    } else {
                        sh 'venv/bin/pytest'
                    }
                }
            }
        }
    }
    post {
        always {
            // Clean up the virtual environment
            script {
                def isWindows = isUnix() ? false : true
                if (isWindows) {
                    bat 'rmdir /s /q venv'
                } else {
                    sh 'rm -rf venv'
                }
            }
        }
        failure {
            echo 'Tests failed!'
        }
    }
}