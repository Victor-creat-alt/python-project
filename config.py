#Import the create_engine object
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#Load Environment Variables
load_dotenv()

#Retrieve Database Credentials from the .env file
user = os.getenv("PG_USERNAME")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
database = os.getenv("PG_DATABASE")

#Function to connect POSTGRESQL using SQLALCHEMY
def get_connection():
    return create_engine(
        url=f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

if __name__ == 'main':
   try:
        # Create an instance of the connection function
        engine = get_connection()
        print(f"Connection to {host} for user {user} created successfully.")
   except Exception as ex:
        print("The connection failed. Please try again later.")
        print("Error details:", ex)
