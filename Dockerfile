# Use Ubuntu as the base image
FROM python:3.11

ENV PYTHONUNBUFFERED=1

# Install Python 3.11 and pip
RUN apt-get update && \
    apt-get install -y python3.11 python3-pip

# Install GDAL dependencies and other required packages
RUN apt-get install -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    libgdal-dev

# Set the GDAL configuration options
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Install GDAL Python package version 3.4.3
RUN pip3 install GDAL==3.4.3

# Copy the application code
COPY . .








