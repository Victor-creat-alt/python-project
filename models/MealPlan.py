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
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    week_number = Column(Integer, nullable=False)
    day_of_week = Column(String(10), nullable=False)  # e.g., "Monday"
    meal_type = Column(String(20), nullable=False)    # e.g., "breakfast", "lunch", "supper"
    planned_meals = Column(String(1000), nullable=False)
    nutrition_balance = Column(String(500), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="meal_plans")
    shared_users = relationship("User", secondary=meal_users, back_populates="shared_meal_plans")

    def __repr__(self):
        return (f"<MealPlan(id={self.id}, user_id={self.user_id}, week_number={self.week_number}, "
                f"day_of_week={self.day_of_week}, meal_type={self.meal_type}, "
                f"planned_meals={self.planned_meals}, nutrition_balance={self.nutrition_balance})>")