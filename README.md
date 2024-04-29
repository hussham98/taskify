


# Taskify: Minimalistic Task Management Web App
## Overview
Taskify is a basic web application built using Flask and Python for managing tasks. This project includes unit tests and utilizes GitHub Actions for continuous integration and continuous deployment (CI/CD) to Heroku.

## Project Structure
- `app.py`: Main Flask application file containing the routes and logic.
- `test_app.py`: Unit tests for testing the application functionality.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory for static files like CSS and JavaScript.
- `Procfile`: Configuration file for Heroku deployment.
- `requirements.txt`: File listing all project dependencies.

## Running the Application
1. Clone the repository:
   ```bash
   git clone <repository_url>
2. Navigate to the project directory:
   ```bash
   cd taskify```

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Set Environment Variables (if necessary):

    ```bash
    export VARIABLE_NAME=value
    ```

5. Run the Application:
    ```bash
    python app.py
    ```

6. Test the Application:
    ```bash
    python test_app.py
    ```

7.  Access the Application:

    Open a web browser and go to view the application.

    ```bash 
    http://localhost:5000
    ``` 
## Pipeline Setup
### GitHub Actions Workflow
The CI/CD pipeline is configured using GitHub Actions, which triggers on every push to the main branch.
It includes linting, testing, and deployment stages.

### Linting and Testing
- Before deployment, the code is checked for linting issues using Flake8.
- Unit tests are run using the `unittest` framework to ensure the correctness of the application.

### Deployment
- Upon successful linting and testing, the application is automatically deployed to Heroku.
- Heroku is chosen for its ease of use and seamless integration with GitHub.

## Manual Deployment
If you wish to deploy the application manually:
1. Ensure your code passes linting and testing stages locally.
2. Commit and push your changes to the main branch.
3. GitHub Actions will automatically trigger the deployment workflow.
4. Once deployment is successful, access the deployed application using the provided Heroku URL.
