from sqlalchemy import Integer, Column, ForeignKey, DateTime, Boolean, Float, func
from sqlalchemy.orm import declarative_base, relationship

Base=declarative_base()

class Report(Base):
    __tablename__ = 'reports'
    #ID uniquely identifies a report
    id = Column(Integer(), primary_key=True)
    user_id=Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    #Stores report date as a TimeStamp
    date=Column(DateTime, server_default=func.now(), unique=True)
    #Calories consumed on a given date
    total_calories=Column(Integer(), nullable=False, default=0)
    #Checks User Status
    goal_status=Column(Boolean, nullable=False, default=False)
    weekly_progress=Column(Float, nullable=False, default='0.0')
    #Auto-generated timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

   #A report can be obtained from multiple users (one-many relationship)=> Bi-directional
    users = relationship('User', back_populates='reports')

    def __repr__(self):
        return f"<Report(user_id={self.user_id}, date={self.date}, total_calories={self.total_calories}, goal_status={self.goal_status}, weekly_progress={self.weekly_progress}, created_at={self.created_at}, updated_at={self.updated_at})"


