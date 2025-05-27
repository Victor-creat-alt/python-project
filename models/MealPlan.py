from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class MealPlan(Base):
    __tablename__ = 'meals'
    id = Column(Integer(), primary_key=True)
    #Link each meal to a specific user and also ensures that database integrity is maintained when a user is deleted
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    week_number=Column(Integer, nullable=False, unique=True)
    planned_meals=Column(String(1000),nullable=False)
    #A planned meal might not require nutrition_balance
    nutrition_balance=Column(String(500), nullable=True)
    created_at=Column(DateTime, server_default=func.now())
    updated_at=Column(DateTime,onupdate=func.now())

    #Relationships
    #Link between meal plans and the particular users
    users = relationship("User", back_populates='meal_plans')

    def __repr__(self):
        return f"<MealPlan(user_id={self.user_id}, week_number={self.week_number}, planned_meals={self.planned_meals}, nutrition_balance={self.nutrition_balance}, created_at={self.created_at}, updated_at={self.updated_at})"
    

