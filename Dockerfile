# Basic Image Environment
FROM python:3.9-slim

# Define environment variables
ENV FLASK_APP=app/server.py

# Copy the files into app
COPY . /app
WORKDIR /app

# Install the dependent libraries
RUN pip install -r requirements.txt

# Start the server
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]