# data-processing-flask
data fetching and processing

This repository contains a simple Flask application that simulates a data retrieval and processing system.

## Project Structure

- `app/`
    - `__init__.py`: Initializes the Flask application.
    - `routes.py`: Contains route definitions.
    - `services.py`: Handles data processing and business logic.
    - `models.py`: Manages in-memory data storage.
- `instance/`
    - `config.py`: Configuration settings for the Flask application.
- `requirements.txt`: Lists the dependencies.
- `README.md`: This file.

## Prerequisites

Ensure you have Python installed.

## Setting Up the Application

1. **Clone the Repository**
   git clone https://github.com/RominGujarati/data-processing-flask.git
   cd data-processing-flask

2. **Create and Activate the virtual environment**
    python -m venv venv
    venv\Scripts\activate

4. **Install Dependencies**    
    pip install -r requirements.txt

5. **Run the Flask Application**
    python app.py


## API Endpoints

Fetch Data
    Endpoint: /fetch-data
    Method: GET
    Description: Simulates fetching data from an external service and processes it.
    Response: Returns the fetched data.


Get Processed Data
    Endpoint: /get-processed-data
    Method: GET
    Description: Retrieves the processed data stored in memory.
    Response: Returns the processed data.