# Email & Push notification microservice
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

# Testing

# Deployment

# Issue

# Contribution

# License
