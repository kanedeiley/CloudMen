# Use the base image that you pushed to your Docker repository
FROM pm926048/csc468.cloud:tagname

# Set the working directory to the root directory of your app
WORKDIR /app

# Copy the files from your local directory to the container
COPY . .

# Specify the command that should be run when the container starts
CMD [ "npm", "start" ]
