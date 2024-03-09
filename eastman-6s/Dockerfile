# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install make
RUN apt-get update && apt-get install -y make

# Run the Makefile
RUN make

# Make port 5000 available to the world outside this container
EXPOSE 5000