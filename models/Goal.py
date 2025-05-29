from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from models import Base

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer(), primary_key=True)
    user_id=Column(Integer, ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    daily_calories=Column(Integer(), nullable=False)
    weekly_calories=Column(Integer(), nullable=False)
    created_at=Column(DateTime, server_default=func.now())
    

    #Linking Goals to a particular user
    user = relationship('User', back_populates='goals')

    def __repr__(self):
        return f"<Goal(user_id={self.user_id}, daily_calories={self.daily_calories}, weekly_calories={self.weekly_calories})>"



