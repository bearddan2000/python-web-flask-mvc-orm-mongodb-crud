# python-web-flask-mvc-orm-mongodb-crud

## Description
Uses ORM from mongodb to create an api.
Two selects are included; one renders the
ORM as JSON the other iterates the properties
one-by-one.

## Tech stack
- python
  - flask
  - mongoengine
- mongodb

## Docker stack
- python:latest
- mongodb

## To run
`sudo ./install.sh -u`
- Endpoints
  - Select as text http://localhost/
  - Select as json http://localhost/json
  - Create by name http://localhost/create/<name>
  - Delete by name http://localhost/delete/<name>
  - Update by name http://localhost/update/<old_name>/<new_name>'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
