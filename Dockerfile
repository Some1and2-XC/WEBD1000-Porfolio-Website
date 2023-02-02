# Set base image (host OS)
FROM python:3.9-alpine

# By default, listen on port 80
EXPOSE 80/tcp
# EXPOSE 443/tcp

# Sets Variables

# Set the working directory in the container
WORKDIR /website

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN pip install -r requirements.txt

# Specify the command to run on container start
# CMD ["gunicorn", "-w", "4", "--bind", "unix:/website/app.sock", "main:app"]
# CMD ["gunicorn", "-w", "4", "--bind", "127.0.0.1:80", "main:app"]
CMD ["python", "deploy_main.py"]