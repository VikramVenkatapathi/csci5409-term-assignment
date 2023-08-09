# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install app dependencies
RUN npm install
RUN npm install react-icons

# Copy the rest of the app's files to the container
COPY . .

# Set the environment variable REACT_APP_API_URL
# ENV REACT_APP_API_URL=

# Expose the port that the React app is listening on (if applicable)
EXPOSE 3000

# Command to start the React app when the container is run
CMD ["npm", "start"]
