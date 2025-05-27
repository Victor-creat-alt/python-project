import typer
from sqlalchemy.orm import sessionmaker
from config import get_connection
from models import User, FoodEntry, Base

app = typer.Typer()
engine = get_connection()
SessionLocal = sessionmaker(bind=engine)