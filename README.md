# Basic REST API Structure

This project provides a basic structure for REST APIs, implementing the Service Object pattern and utilizing Pytest for automated testing.

## Requirements

- Python 3.8 or higher.

## Installation

1. Clone the repository.
2. Navigate to the project's root directory.
3. Install the dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```
## Usage
To execute the tests, follow the steps below:

Navigate to the project's root directory.

### Single execution - Execute the following command for :
   ```bash
      pytest
      or 
      pytest ./tests/test_{file_name}.py
   ```

### Parallel execution - Execute the following command for :
   ```bash
      pytest -n {worker quantity to execute in parallel}
      Ex: 
      pytest -n 5
   ```
Note: Check the time consumed using single parallel execution in.

### Generate report:
   ```bash
      pytest --html=report.html
      or 
      pytest ./tests/test_{file_name}.py --html=report.html
      or 
      pytest -n 5 --html=report.html
   ```
Note: Check the time consumed using single parallel execution in.

## Running on Docker
1. Install the docker
2. Access the pytest-rest-api, in the same level of Dockerfile
   3. Run the docker command to create an image:
   ```
      docker build -t <image_name> .

      ex: docker build -t pytest-rest .
   ```
   Command to check the images: docker images
    ```
        docker images
   ```
   4. Run the container:
   ```
      docker run --rm <image_name>
      
      ex: docker run --rm pytest-rest
   ```
   Command to check the containers running
   ```
   docker ps
   ```
3. (Optional) Mount a volume to access the HTML report on your host machine:

   1. Create a package in the root with the name reports;
   2. Replace the $(pwd) or pwd for your project pash:
      2. Ex: pwd -> C:/Users/YOUR_USER/project/pytest-rest-api
```bash
     docker run --rm -v <YOUR_PROJECT_PATH>/reports:/usr/src/app/reports pytest-selenium pytest -s -v --log-level=info --tb=auto --html=reports/report.html --self-contained-html
```
- -v <YOUR_PROJECT_PATH>/reports:/usr/src/app/reports: Mounts the reports directory on your host to /usr/src/app/reports in the container.

- The HTML report will be saved in the reports directory on your host.

The .html will be stored inside the reports folder
### Note: 

The Dockerfile contain the [ENTRYPOINT] and [CMD] values.
This means you don't have to pass all these commands AGAIN, but if you do, the default values 
will be overwritten.

## Project Structure
The project is organized into layers to promote separation of concerns:

- [tests/]: Contains unit and integration tests, responsible for:
  - Defining input data for tests. 
  - Making requests to the API. 
  - Validating API responses through assertions.

- [service/]: Implements the service layer, responsible for:
  - Managing business logic and operations before making API requests.
  
- [base_service/]: Provides a base class with generic methods for API interaction (GET, PUT, POST, etc.), facilitating the implementation of specific services.

- [helpers/]: Contains only common functions

- [conftest.py]: Contains all functions related to setup and tear down from (Pytest, Pytest-html, Pytest-xdist)