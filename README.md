# hng_stage_two
## Description
This is a straightforward REST API designed for executing CRUD (Create, Read, Update, Delete) operations on a "person" resource.
## Programming languages and databases
programming language: python 
web frameworks: django
database: dbsqlite
## Set Up
1. Clone this repository.
2. Install project dependencies using pip install -r requirements.txt.
3. Run application using 'python manage.py runserver'
## Endpoints
### Create Person (POST)

 Route: /api

 Method: POST

 Description: Adds a new person to the database.

### Find Person (GET)

Route: /api/:userID

Method: GET

Description: Retrieves a person's information using their userID.

### Update Person (PUT)

Route: /api/:userID

Method: PUT

Description: Updates a person's details.

### Delete Person (DELETE)

Route: /api/:userID

Method: DELETE

