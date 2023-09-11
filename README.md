
# CRUD Application Documentation

Welcome to the documentation for our CRUD (Create, Read, Update, Delete) application. This documentation provides an overview of the CRUD operations, setup instructions for Windows, Linux, and macOS users, and includes a section on UML diagrams.

## Setup

 Follow the instructions below to setup the application on your local machine.

### Windows

1. **Install Python:** Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:** Use `git clone` to clone the application repository.

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

            pip install -r requirements.txt

### Linux & macOS

1. **Install Python:** Most Linux distributions and macOS come with Python pre-installed. You can verify by running `python --version`.

2. **Clone the Repository:** Use `git clone` to clone the application repository.

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

          pip install -r requirements.txt

## Database Setup

The application uses MongDB as its database. You can download and install MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community).

After installing MongoDB, you add the following environment variables to your system:

    DATABASE_URI: The URI for your MongoDB database.
    DATABASE_NAME: The name of your MongoDB database.
    COLLECTION_NAME: The name of your MongoDB collection.

## Running the Application

After setting up the application, you can run it by running the following command in the project directory:

    python app.py

## Testing

You can run a quick test after  starting the application by running the following command in a new terminal:
  
      python Test.py <url>

## API Documentation

Click the [link](https://github.com/blacdev/HNG_Stage_Two/blob/staging/DOCUMENTATION.md) to read the api documentation.

## UML Diagrams

We have provided UML diagrams for a visual representation of our application's structure. You can find the UML diagrams in the link below.

[UML Diagrams](https://drive.google.com/file/d/1OBUdOP8uOIFK4KRb7FYqgTAUAhnLNm6-/view?usp=sharing)
