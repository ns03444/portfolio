# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary dependency files first
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application files
COPY . /app

# Expose the port Flask runs on
EXPOSE 5000

# Define the entrypoint command
CMD ["poetry", "run", "python", "app.py"]
