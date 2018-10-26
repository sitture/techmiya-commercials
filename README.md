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

## Production Configuration with Docker

### Prerequisites

[Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
[Docker Compose](https://docs.docker.com/compose/install/)

### Codebase dependent deployment with docker

```bash
git clone https://github.com/sitture/techmiya-commercials.git

cd techmiya-commercials/

docker-compose up -d
```

### Codebase Independent Deployment with docker images

Create docker Image of the application

```bash
git clone https://github.com/sitture/techmiya-commercials.git

cd techmiya-commercials/

docker build -t techmiya-commercials .

```

Check the images created

```bash
docker images
```

Create `docker-compose.yml` for deployment with docker images

```bash
version: "2.1"
services:

  db:
    image: mysql/mysql-server:5.7
    container_name: techmiya-db
    env_file:
      - ./.env
    healthcheck:
      test: ["CMD", "mysqladmin" ,"ping", "-h", "localhost"]
      timeout: 20s
      retries: 10

  app:
    image: techmiya-commercials
    container_name: techmiya-commercials
    env_file:
      - ./.env
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy

```

Run the app

```bash
cd techmiya-commercials/
docker-compose up -d
```
