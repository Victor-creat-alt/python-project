from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve database credentials from the .env file
user = os.getenv("PG_USERNAME")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
database = os.getenv("PG_DATABASE")

# Validate environment variables before proceeding
if not all([user, password, host, port, database]):
    raise ValueError("Missing one or more required environment variables. Check your .env file.")

# Function to connect PostgreSQL using SQLAlchemy
def get_connection():
    return create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{database}",
        echo=True,  # Enable debug output (optional)
        pool_pre_ping=True  # Ensures persistent connection handling
    )

if __name__ == "__main__":
    try:
        # Create an instance of the connection function
        engine = get_connection()
        print(f"Connection to {host} for user {user} created successfully.")
    except Exception as ex:
        print("The connection failed. Please try again later.")
        print("Error details:", ex)