from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

Base = declarative_base()

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    id= Column(Integer(), primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    food_name=Column(String, nullable=False)
    calories=Column(Integer(2000), nullable=False)
    date = Column(DateTime, server_default=func.now())
    meal_type=Column(String, nullable=False)
    quantity=Column(Integer, nullable=False)
    created_at=Column(DateTime, server_default=func.now())

    #Linking FoodEntries to Users
    users = relationship('User', back_populates='food_entries')

    def __repr__(self):
        return f"<FoodEntry(user_id={self.user_id}, created_at={self.created_at}, food_name={self.food_name}, calories={self.calories}, date={self.date}, meal_type={self.meal_type}, quantity={self.quantity})>"
