# Use latest Python runtime as a parent image
FROM python:3.6.5-slim

# Meta-data
LABEL maintainer="Aly Sivji <alysivji@gmail.com>" \
      description="Data Science Workflow #1: Self-Contained Container\
      Libraries, data, and code in one image"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required libraries
RUN pip install --upgrade pip && pip --no-cache-dir install numpy pandas seaborn sklearn jupyter

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]

# Build the container with: docker build -t iris-data .
# Run the container with: docker run -p 8888:8888 iris-data
