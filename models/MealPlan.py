from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

#An Association table that links users to many meals
meal_users = Table(
    'meal_users',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('meal_id', Integer, ForeignKey('meal_plans.id', ondelete='CASCADE') )
)

class MealPlan(Base):
    __tablename__ = 'meal_plans'
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
    users = relationship("User", secondary=meal_users,  back_populates='meal_plans')

    def __repr__(self):
        return f"<MealPlan(user_id={self.user_id}, week_number={self.week_number}, planned_meals={self.planned_meals}, nutrition_balance={self.nutrition_balance}, created_at={self.created_at}, updated_at={self.updated_at})>"
    

