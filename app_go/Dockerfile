# use the official Golang image to build and run the application
FROM golang:1.23-alpine

# set the working directory inside the container
WORKDIR /app

# copy the project files to the working directory
COPY app.go index.html go.mod .

# Create a directory for the visits file
RUN mkdir -p /data

# Ensure the visits file exists
RUN touch /data/visits.txt

# download dependencies and compile the application
RUN go mod download && go build -o app

# expose port 8000 to access the app
EXPOSE 8000

# run the app when the container starts
CMD ["./app"]
