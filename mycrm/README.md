# MyCRM

**MyCRM** is a customer relationship management system built with Django and Python. The system is designed to manage and organize customer data efficiently. It features a user-friendly interface to facilitate seamless interaction with customer information and can scale with business needs.

## Features

- Manage customer profiles and data
- User-friendly interface with Django templates
- Built-in reporting and customer analytics
- Supports MySQL database for data storage

## Technologies Used

- **Python**: Programming language for the backend logic
- **Django**: Web framework for building the web application
- **MySQL**: Database for storing customer data

## Installation

To run the project locally, follow these steps:

### Prerequisites

- Python 3.x installed on your system
- MySQL installed and running

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/se-thato/crm.git
   cd crm



### Create and activate a virtual environment:
- python3 -m venv virt
- source venv/bin/activate  # On Windows: virt\Scripts\activate


### Install the required dependencies:
- pip install -r requirements.txt

### Set up the MySQL database:
- Create a new database in MySQL.
- Update the DATABASES setting in settings.py to match your MySQL credentials.


### Apply the migrations:
- python manage.py migrate

### Create a superuser to access the Django admin interface:
- python manage.py createsuperuser

### Run the development server:
- python manage.py runserver
- Access the application at http://127.0.0.1:8000/ and log in with the superuser credentials.

### Dependencies
### The following packages are required for the project:

- asgiref: 3.8.1
- Django: 5.1.3
- mysql: 0.0.3
- mysql-connector: 2.2.9
- mysql-connector-python: 9.1.0
- mysqlclient: 2.2.5
- pip: 23.2.1
- sqlparse: 0.5.1
- tzdata: 2024.2
