# Use Python as base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files from host to image
COPY . /app

# Install dependencies during build
RUN pip install --no-cache-dir flask

# Document the port used by Flask app
EXPOSE 5000

# Default command when container starts
CMD ["python", "app.py"]
