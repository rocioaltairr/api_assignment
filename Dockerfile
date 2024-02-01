FROM python:3.11.7

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port
EXPOSE 5000

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]