"""
From 30 Days of Python tutorial, made by Coding Entrepreneurs.

Day 14 - Web App with Flask, FastAPI, ngrok and Invictify

Making a web app
"""

# Run a web server in python. Allows the 8000 port in localhost to access by a web browser

    $ python -m http.server

# To make and run an executable file and simplify the command writing to start a server

    $ echo "gunicorn server1:app" > server1.sh
    $ chmod 775 server1.sh
    $ ./server1.sh

# To add an alias command to system bash file

    $ sudo nano ~/.bashrc
    # Example to add an alias to the bash file
    alias ngrock="/path-to-executable-file/ngrock"
    $ source ngrock

1) Virtual environment
----------------------

First you need to get into the project folder to use pipenv. The project apps are running in a virtual environment initialized with:

    $ cd ~/projects/project-name
    $ pipenv shell

As we have been using our own virtual environment, we going to activate it and then use pipenv to initialize the Pipfile

    $ source ~/python_environment/bin/activate
    (python_environment) $ pipenv shell

2) Requirements
---------------

    This project use the next packages: flask, gunicorn, uvicorn, fastapi, to install we can use:

    (python_environment) $ pipenv install flask gunicorn uvicorn fastapi

    In this case pipenv going to install the packages in python_environment and then update the Pipfile file and create the Pipfile.lock file with the requirements.

2) Run a web app in Flask using gunicorn
----------------------------------------

    First you need to create your web application, at this case can use server1.py. Then you can run it:

    (python_environment) $ gunicorn server1:app --bind 127.0.0.1:8000

    Where the server start and allows the localhost:8000 or http://127.0.0.1:8000 in the web browser

3) Run a web app in FastAPI using uvicorn
-----------------------------------------

    In this case use server2.py to create the FastAPI application. Then you can run it:

    (python_environment) $ uvicorn server2:app --port 8000 

    Where the server start and allows the localhost:8000 or http://127.0.0.1:8000 in the web browser. You can make a bash executable file to run this command easly

4) Use ngrock to allow the web server started with gunicorn or uvicorn on internet
----------------------------------------------------------------------------------

    This is other terminal. First your need to register and download ngrock: https://dashboard.ngrok.com/signup, once downloaded the zip file, move it to development (or projects) folder

    $ mv ~/Downloads/ngrock-name-file.zip ~/projects

    Renaming the zip the file to ngrock.zip, then unzip it and configure to connect to your ngrock account

    $ mv ~/projects/ngrock-name-file.zip ~/projects/ngrock.zip
    $ unzip ~/projects/ngrock.zip
    $ cd ~/projects/ngrock/
    $ ./ngrock authtoken use_your_token_here

    You can define an alias in your bash file to run this executable file more easly

    Use ngrock to allow your server to access by a valid route on internet:

    $ ./ngrock http 8000

    And you need to run your server in other terminal, then back to our project folder:

    (python_environment) $ gunicorn server1:app

    Or:

    (python_environment) $ uvicorn server2:app

5) Invictify
------------

    Is an scheduler task web service available in https://invictify.com, where you introduce an url to your project and the scheduler execute a request every specified unit of time. This web service have a administrative panel where show the response of the every task executed.