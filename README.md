[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


A simple email and push notification microservice made with Django.

# Features
- [ ] Send Emails (SMTP).
  - [ ] Bulk email services like newsletter, service emails.
  - [ ] Scheduled email.
  - [ ] Email template dashboard to create and upload emails.
- [ ] Push notification (Firebase push notification).
  - [ ] Send bulk notification to user.
  - [ ] Send scheduled notifications.
  - [ ] Create notification template in dashboard.
- [ ] Create entry of user subscribed to different services in the database.
- [ ] Analyse user activity on email and notification clicks to send recommendation email and notification based on user preferences. 
- [ ] Implement a library to integrate this microservice to an existing project.

## Future plans
- Add support to custom push notification.
- Add support for email services like ZOHO to send emails.

# Installation

## Pre-requisite

- [Git](https://git-scm.com/downloads) - For version control
- [VS-code](https://code.visualstudio.com/download) - Recommended
- [python3.7](https://www.python.org/downloads/release/python-370/)
- [poetry](https://python-poetry.org/docs/#installation) (optional if using docker)
- [Docker](https://www.docker.com/get-started) (optional)

## Local development setup

### Using Docker

1. Clone this repository.
   ```bash
   git clone https://github.com/namantam1/email-notification-microservice
   cd email-notification-microservice
   ```
2. Run this command to build and start docker container.
   ```bash
   docker-compose up
   ```

### Without Docker (Poetry is needed for it)

1. Clone this repository.
   ```bash
   git clone https://github.com/namantam1/email-notification-microservice
   cd email-notification-microservice
   ```
2. Install [Poetry](https://python-poetry.org/docs/#installation).
3. Set Poetry config to make virtual environment inside project (Optional).
   ```bash
   poetry config virtualenvs.in-project true
   ```
4. Install the dependency.
   ```bash
   poetry install
   ```
5. Run local server.
   ```bash
   poetry run python manage.py runserver
   ```

## Development Guidelines

### Configuration Variables
All the configuration like secret key, database, etc are all setup using [django-environ](https://github.com/joke2k/django-environ), all these configuration are take from `.env` file in the root directory.

To setup configuration, look into `.env.dist` file.

While local development copy `.env.dist` into `.env` file with your own requirements.

> **NOTE:** Please don't commit `.env` file into version control.

### Dependency Management

We are using [Poetry](https://python-poetry.org) as our default package manager for managing all Python dependencies.

- Add any dependency using.
  ```bash
  poetry add <dependency name>
  ```
- If add any new dependency which is required in production update `requirements.txt` file also.
  ```bash
  poetry export --without-hashes -o requirements.txt
  ```
> **Important:** Please insure that `requirements.txt` does not includes dev dependencies as it increase the container size of application otherwise delete `poetry.lock` and run `poetry install` to generate the new `poetry.lock` file, then follow above procedure to get it done.

- Add dependency as dev dependency if not required in production.
  ```bash
  poetry add --dev <dev dependency name>
  ```

### Pre-Check before pushing the code to gitHub
1. Insure that you have not included any confidential file or data before pushing.
2. Write the test if possible and insure all test case passes before pushing.
3. Make sure your code is well formatted with `black` before pushing to avoid build error.
   ```bash
   black . # run inside base directory
   ```

## Testing Guidelines

# Deployment

## Server Deployment
To deploy on server like EC2, Google cloud, etc clone the master branch, set config variables in `.env` file and run.
```bash
docker-compose -f docker-compose.prod.yaml up -d
```

This will start the server which can be listen on port 80.

> To use custom port set environment variable `PORT=<custom_port>` in `.env` file.

## Heroku Deployment

# Issue

# Contribution

# License
