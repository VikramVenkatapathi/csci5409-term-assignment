# Stage 1: Use the official AWS CLI Docker image to copy AWS CLI and SDK tools
FROM amazon/aws-cli:latest AS awscli

# Set AWS credentials as build arguments
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION

# Set environment variables using build arguments
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_REGION=$AWS_REGION

# Stage 2: Use the base Python image as the final image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /file

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend application code to the container
COPY . .

# Expose the port your backend application is running on
EXPOSE 5000

# Command to run your backend application
CMD ["python3", "-m","main", "run", "--host=0.0.0.0", "--port=5000"]
