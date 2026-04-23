# Use python as base image

FROM python:3.11-slim

# Set work directory inside contanier

WORKDIR /app

# Copy project host to image

COPY . .

# Install dependenceins during build 

RUN pip install -r requirements.txt

# Expose the port used by Flask app

EXPOSE 5000

# run the command 

CMD ["python", "app.py"]
