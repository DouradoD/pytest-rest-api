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