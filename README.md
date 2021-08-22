# Library
[![Django CI](https://github.com/TheLe0/library/actions/workflows/build.yml/badge.svg)](https://github.com/TheLe0/library/actions/workflows/build.yml)

This is a REST API made on Django REST Framework, for a library system. Storing books and its authors.

## Specification

This project was built with:

* Python - 3.8.10
* SQLite - 3.31.1
* Virtualenv - 20.0.17
* PIP - 20.0.2

> Note:
> You have to install this dependencies to run the API on your machine. Only the SQLite you don't need to install, is going to work without too.


## Setup and Installation

1. First create a virtualenv on the project root

```pycon

virtualenv venv

```

Once created, activate it:

```pycon

source venv/bin/activate

```

> Note:
> **venv** is the name of the virtual enviroment that you created, you can put whatever name you want. 

2. In ``` ./libapi/libapi/ ``` folder, create a ``` .env ``` file, to put the enviroment variables that you are going to need to run.

```
SECRET_KEY=
USERNAME=
EMAIL=
PASSWORD=
```

Where:

* SECRET_KEY: The key generated by Django to generate hashed.
* USERNAME, EMAIL and PASSWORD: Is the data used for create the super user on Django Admin.

3. The file ``` ./data/authors.csv ```, is a list of authors to create on the database, this is done during the migration.
The CSV file will have the following format:

```
name
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K Rowling
```

4. Install the dependencies for the project, on ``` requirements.txt ```, with the following command:

```pycon
pip install -r requirements.txt
```

5. Do the migrations for create the local database. You need to be in this directory ``` ./libapi ``` 

```pycon
python manage.py migrate
```

6. And finally your project is ready to go, now you only need to start the webserver:

```pycon
python manage.py runserver 
```
> Note:
> This will start the server on the defaults hostname and port. If you want to specify where the server is going to point, in the end of the command put ``` YOUR_HOSTNAME:YOUR_PORT```

## Endpoints ##

The API has only three endpoints:
* **admin/** : to access the admin page with the super user created
* **authors/** : List all the authors in the database, with the option to filter by name
* **books/** : Complete CRUD endpoint for the Book entity

All the endpoints are:

**GET**

* **authors/** - List all the authors (You can search with the parameter name)
* **books/** - List all the books (You can search with the parameters name, edition, publication_year and author)

> Note:
> The list endpoints are paginated

**POST**

* **books/** - Create a new book

Input JSON:
```
{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": // List of author ids, same ids of previous imported data
}
```

**DELETE**

* **books/id/** - Delete a book data by its id

**UPDATE**

* **books/** - Update a book data by its id

Input JSON:
```
{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": // List of author ids, same ids of previous imported data
}
```
