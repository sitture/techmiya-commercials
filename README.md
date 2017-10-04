# techmiya-commercials

[![Build Status](https://travis-ci.org/sitture/techmiya-commercials.svg?branch=master&style=flat-square)](https://travis-ci.org/sitture/techmiya-commercials) [![Requirements Status](https://requires.io/github/sitture/techmiya-commercials/requirements.svg?branch=master)](https://requires.io/github/sitture/techmiya-commercials/requirements/?branch=master)

A Django-based website for http://techmiyacommercials.com

## How to setup

Follow this guide to setup this project on your local machine.

1. Install [python] 2.x, git and [virtualenv] in your computer.

2. Get the source code on your machine by-

    `git clone https://github.com/sitture/techmiya-commercials.git`

3. Create a python virtual environment and install python and django related dependencies.

    ```shell
    cd techmiya-commercials
    virtualenv venv # create virtual env
    source venv/bin/activate  # run this command everytime before starting on the project
    pip install -r requirements/dev.txt
    ```
4. For creating database migrations run

    `python manage.py migrate`

    `python manage.py makemigrations`

5. For running the server

    `python manage.py runserver`

6. Open the browser and got to the following link.

    `127.0.0.1:8000`


[virtualenv]: https://virtualenv.pypa.io/
[python]: https://www.python.org/downloads/release/python-2713/
