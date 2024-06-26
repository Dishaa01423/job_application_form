# Job Application Form using Django

This repository contains a Django-based web application for submitting job applications. Users can fill out and submit job application forms, and administrators can view and manage the submissions.

## Features

- User-friendly job application form
- Admin interface for managing job applications
- Email notifications for new applications (optional)

## Prerequisites

- Python 3.x
- Django
- PostgreSQL (optional, for production setup)

## Setup

### Clone the repository

```sh
git clone https://github.com/your-username/job-application-form.git
cd job-application-form
```
## Create and activate a virtual environment
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

## Install dependencies
```sh
pip install -r requirements.txt
```

## Configure the database
1. SQLite (default): The project is configured to use SQLite by default.

2. PostgreSQL (optional): If you prefer PostgreSQL, update DATABASES in mysite/settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your-db-name',
            'USER': 'your-db-user',
            'PASSWORD': 'your-db-password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
## Apply migrations
```sh
python manage.py migrate
```

## Create a superuser
```sh
python manage.py createsuperuser
```

## Run the development server
```sh
python manage.py runserver
```

## Usage
**Submitting Job Applications**

Users can fill out and submit job application forms through the web interface.

**Managing Job Applications**

Admin users can view and manage job application submissions from the admin interface.

## Deployment

1. Collect static files:

```sh
python manage.py collectstatic
```

2. Set up a production server: Use a web server like Gunicorn with Nginx or Apache for deployment.

3. Environment variables: Ensure you set the necessary environment variables for Django settings, such as SECRET_KEY, DEBUG, and ALLOWED_HOSTS.
