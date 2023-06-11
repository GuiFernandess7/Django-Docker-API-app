# Django-Docker-API-app
    
#### Tools Used:
* Django
* Flask
* Docker

### Description: 

This project utilizes Django, Flask, and Docker to create a web application. It consists of two main components: an API built with Django Rest Framework and an application built with Flask. The project leverages Docker for containerization, providing an isolated and reproducible environment.

### API (Django):

* Provides endpoints for functionalities such as creating contact entries, items and stocks
* Utilizes Django's models, serializers, and views

### APP (Flask):

* Serves as a separate service alongside the Django API
* Provides a simple endpoint ("/") returning a "Hello DRF!" message

### Docker (Containers):
* Two Docker containers: one for the Django API and another for the Flask application
* Docker Compose file defines services, network, and dependencies
* Containers are built based on Dockerfiles and connected via an internal network

### To run the project, follow these steps:

* Clone the repository.

* Install Docker on your system.

* Navigate to the project directory (backend)

* Run the command: 

```
docker-compose up -d --build
```

Access the Flask application at http://localhost:5000

Interact with the Django API at http://localhost:8000

### API communication and post request between Flask and Django containers:

In the described scenario, where there are two containers running—one for the Flask application and another for the Django API—communication between them is facilitated by Docker's internal network.

When you run the containers using Docker Compose or Docker, they are placed in the same internal network, allowing communication between them using the service names defined in the Docker Compose configuration file.

To make a request from the Flask container to the Django API container, you can use the service name defined in the Docker Compose file as the hostname. For example, if the service name for the Django API container is api, you can make a request to http://api:8000/endpoint within the Flask container terminal:

```
http http://api:8000/contact/ name='Your name' message='test' email='youremail@email.com'
```

This works because Docker Compose automatically sets up a DNS resolver that maps the service names to the IP addresses of the respective containers within the internal network. By referring to the Django API container by its service name, you can seamlessly interact with it from the Flask container.

### Result of the post request:

<img width="771" alt="Captura de tela 2023-06-04 181522" src="https://github.com/GuiFernandess7/Django-Ecommerce-API/assets/63022500/c494c2e5-ce66-4162-898d-b57fa87b873b">

