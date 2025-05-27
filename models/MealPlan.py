from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import relationship
from models import Base

# Many-to-Many Association Table Connects users with their meals as database integrity is maintained
meal_users = Table(
    'meal_users',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id', ondelete="CASCADE"), primary_key=True),
    Column('meal_id', Integer, ForeignKey('meal_plans.id', ondelete="CASCADE"), primary_key=True)
)

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    # Primary Key - Unique identifier for each meal plan
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign Key - Links meal plans to users (for One-to-Many)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    # Week number - Represents the week of the year (one meal plan per week)
    week_number = Column(Integer, nullable=False, unique=True)
    # Planned meals - Stores meal preparation details
    planned_meals = Column(String(1000), nullable=False)
    # Nutritional balance - Meal classification (optional)
    nutrition_balance = Column(String(500), nullable=False)
    # Auto-generated timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="meal_plans")
    shared_users = relationship("User", secondary=meal_users, back_populates="shared_meal_plans")

    def __repr__(self):
        return f"<MealPlan(id={self.id}, user_id={self.user_id}, week_number={self.week_number}, planned_meals={self.planned_meals}, nutrition_balance={self.nutrition_balance})>"