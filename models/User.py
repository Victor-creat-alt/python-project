from sqlalchemy import Integer, String, Column, DateTime, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    #Name of the database
    __tablename__ = 'users'
    #ID uniquely identifies a user
    id = Column(Integer(), primary_key=True)
    name = Column(String(500), unique=True, nullable=False)
    created_at = Column(DateTime,server_default=func.now())

    #One to many relationship between User and Food Entry(A user can make multiple food entries)
    food_entries = relationship('FoodEntry', back_populates='users', cascade='all, delete-orphan')

    #One to many relationship between User and report(A user can make multiple reports)
    reports = relationship('Report', back_populates='users', cascade='all, delete-orphan')

    #One to many relationship between User and Goal(A user can have multiple goals)
    goals = relationship('Goal', back_populates='users', cascade='all, delete-orphan')

    #A user can make multiple meal plans
    meal_plans = relationship('MealPlan', back_populates='users', cascade='all, delete-orphan')

    #Actual Representation of user Attributes
    def __repr__(self):
        return f"<User(name={self.name}, created_at={self.created_at})>"

    

