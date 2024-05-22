
Figure 17.1: The Docker Desktop interface

After installing Docker Compose, you will need to create a Docker image for your Django project.

Creating a Dockerfile
You need to create a Docker image to run the Django project. A Dockerfile is a text file that contains the commands for Docker to assemble a Docker image. You will prepare a Dockerfile with the commands to build the Docker image for the Django project.

Next to the educa project directory, create a new file and name it Dockerfile. Add the following code to the new file:

# Pull official base Python Docker image
FROM python:3.12.3
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set work directory
WORKDIR /code
# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy the Django project
COPY . /code/