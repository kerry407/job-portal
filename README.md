# Job Portal API

This is a RESTful API built with Django Rest Framework for a job portal. It allows users to browse and apply for available jobs, as well as create, update, and delete job listings.

## Features

- Search job postings based on job title, company, location, or other keyword
- Submit applications for job postings
- Create new Job Post
- Manage job applications

## Requirements

- Python 3.6+
- Django 2.2+
- Django Rest Framework 3.9+

## Installation

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/job-portal-api.git
```

2. Install the requirements:

```
pip install -r requirements.txt
```

3. Migrate the database:

```
python manage.py migrate
```

4. Run the server:

```
python manage.py runserver
```

## Usage

Once the server is running, you can access the API by navigating to http://localhost:8000/ in your web browser.

## Endpoints
The API provides the following endpoints:

### POST: api/auth/sign-up/
Allows anyone to create an account

### POST: api/auth/login/
Allows a user to login. An access token and a refresh token is generated.

### POST: api/auth/login/refresh/
Allows a user to create a new access token with a refresh token.

### GET: api/dasboard/job-list/
Retrieves a list of all jobs currently listed on the portal.

### POST: api/dashboard/post-job/
Creates a new job listing on the portal.

### GET: api/dashboard/job-post-detail/{job_slug}/
Retrieves details of a specific job listing.

### PUT/PATCH: api/dashboard/job-post-detail/{job_slug}/
Updates a specific job listing.

### DELETE: api/dashboard/job-post-detail/{job_slug}/
Deletes a specific job listing.

### POST: api/dashboard/apply-job/{job_slug}/
Allows a user to apply for a specific job listing.

### GET: api/dashboard/job-application-list/
Allows a user to view list of applied jobs. 

### GET: api/dashboard/job-application-detail/{job_application_id}/
Allows both a user and a job poster to view a specific job application. 

### PUT/PATCH: api/dashboard/job-application-detail/{job_application_id}/
Allows only a job poster to update a specific job application. 

### DELETE: api/dashboard/job-application-detail/{job_application_id}/
Allows only a job poster to delete a specific job application. 

# Authentication

The API requires authentication to perform certain actions. To authenticate, you can use the built-in Django Rest Framework authentication system. You can create a new user by sending a POST request to the `api/auth/sign-up/` endpoint, and then authenticate using a POST request to the `api/auth/login/` endpoint. Once you are authenticated, you can include your token in the Authorization header of your requests to access protected endpoints.

# Contributing

Contributions to the API are welcome. To contribute, please fork the repository and submit a pull request with your changes. Please make sure to include tests for any new functionality.
