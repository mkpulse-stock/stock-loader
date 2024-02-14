# Basic Image Environment
FROM python:3.9-slim

# Copy the files into app
COPY . /app
WORKDIR /app

# Install the dependent libraries
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start the server
EXPOSE 8080
CMD ["python", "main.py"]