# Django Ecommerce API

Tools Used
* Django
* Flask
* Docker

### Description: 

This project utilizes Django, Flask, and Docker to create a web application. It consists of two main components: an API built with Django Rest Framework and an application built with Flask. The project leverages Docker for containerization, providing an isolated and reproducible environment.

### API (Django):

* Provides endpoints for various functionalities such as creating contact entries
* Utilizes Django's models, serializers, and views
* Application (Flask):

### APP (Flask):

* Serves as a separate service alongside the Django API
* Provides a simple endpoint ("/") returning a "Hello DRF!" message
* Docker:

### Docker (Containers):
* Two Docker containers: one for the Django API and another for the Flask application
* Docker Compose file defines services, network, and dependencies
* Containers are built based on Dockerfiles and connected via an internal network

To run the project, follow these steps:

Clone the repository.
Install Docker on your system.
Navigate to the project directory.
Run the command: docker-compose up
Access the Flask application at http://localhost:5000
Interact with the Django API at http://localhost:8000

