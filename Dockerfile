# Use an official Python runtime as a parent image
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY src /app

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH=/app

# Run tests
RUN pytest --disable-warnings

# Use a lightweight version of Python runtime for the final image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the installed dependencies and the application from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/flask /usr/local/bin/flask
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 2000

# Define the command to run the application
CMD ["python3", "run.py"]

