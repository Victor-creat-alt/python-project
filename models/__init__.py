from sqlalchemy.orm import declarative_base

# Define Base here
Base = declarative_base()

# Import models
from .User import User
from .Report import Report
from .MealPlan import MealPlan
from .Goal import Goal
from .FoodEntry import FoodEntry

# Expose modules for imports
__all__ = ["Base", "User", "Report", "MealPlan", "Goal", "FoodEntry"]