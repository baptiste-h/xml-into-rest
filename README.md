# xml-into-rest

Django app importing XML file data to be displayed through endpoints.

## Installation

- `git clone <repository-ul>` - Clone this repository

- `cd xml-into-rest`

- `python3 -m venv env` - Setup environment

  ( or `python -m venv env` )

- `source env/bin/activate` - Start environment

- `pip install -r requirements.txt` - Install dependencies

- `cd project`

- `python manage.py migrate` - Setup database

## Running

From `project` folder root :

- Start dev server

  `python manage.py runserver`

- Import data from XML file located at project root

  `python manage.py import_xml orders-test.xml`

- View orders at `http://127.0.0.1:8000/api/order/`

- View specific order at `http://127.0.0.1:8000/api/order/<id>/`

- Run tests

  `python manage.py test orders.tests`

- Run ruff

  `ruff check`

## Admin

To view and edit data :

- Access admin at `http://127.0.0.1:8000/admin/`

- Create admin (email can be left blank)

  `python manage.py createsuperuser`

- Log into django admin with your credentials
