# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to avoid interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Specify the command to run the Streamlit app on container start
CMD ["streamlit", "run", "streamlit/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
