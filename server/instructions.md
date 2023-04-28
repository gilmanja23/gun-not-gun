# Install Virtual Env

    1. cd into server directory
    2. run the following: "python3 -m venv venv"

# Install Requirements:

    3. pip install -r requirements.txt

# To start the server run:

    4. uvicorn main:app --reload

    http://127.0.0.1:8000/docs

    - Gives access to the api structure

# All commands after this point are for development, not running the app.

# Add new packages:

    pip freeze > requirements.txt
