# Use latest miniconda image as parent
# miniconda is python + conda installer
FROM continuumio/miniconda3

# Meta-data
LABEL maintainer="Aly Sivji <alysivji@gmail.com>" \
      description="Docker Data Science Workflow #2: Data Science Project\
      Libraries inside image. Data/code mounted via shared folder.\
      Easy to set up a new developmenet environment."

# Set the working directory to /app
WORKDIR /app

# Install the required libraries
RUN conda install jupyter -y && \
    conda install pandas -y && \
    conda install matplotlib -y && \
    conda install seaborn -y && \
    conda install scikit-learn -y && \
    conda clean -y --all

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Create mountpoint
VOLUME /app

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]

# Build the contaner: docker build -t test-mount .
# Run the container (**Be sure to replace <directory-with-the-lab> with your own path! Which port are you using on the host?**): docker run -p 9999:8888 -v  /<absolute-path-to-the-directory-with-the-lab>:/app test-mount
# For me: docker run -p 9999:8888 -v /home/adaltas/Documents/teaching_material/mlops/modules/11.docker-containers/lab-resources/example2-data-science-project/test_docker_vol:/app test-mount
