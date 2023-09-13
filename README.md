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

Route: /api/:ID

Method: GET

Description: Retrieves a person's information using their userID.

### Update Person (PUT)

Route: /api/:ID

Method: PUT and PATCH

Description: Updates a person's details.

### Delete Person (DELETE)

Route: /api/:ID

Method: DELETE

### UML diagram
https://lucid.app/lucidchart/097e1f1f-1609-46c6-92f4-335d42a8476a/edit?viewport_loc=-11%2C-11%2C1480%2C697%2C0_0&invitationId=inv_82b2ac9a-7f8a-4cbe-9126-48d8803d1793

