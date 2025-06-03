from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    food_entries = relationship("FoodEntry", back_populates="user", cascade="all, delete-orphan")
    reports = relationship("Report", back_populates="user", cascade="all, delete-orphan")
    goals = relationship("Goal", back_populates="user", cascade="all, delete-orphan")
    meal_plans = relationship("MealPlan", back_populates="user", cascade="all, delete-orphan")

    # Many-to-Many Relationship (Shared Meal Plans)
    shared_meal_plans = relationship("MealPlan", secondary="meal_users", back_populates="shared_users")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, created_at={self.created_at})>"