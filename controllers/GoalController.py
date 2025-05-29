from models.Goal import Goal
from sqlalchemy.orm import Session

def create_goal(session: Session, user_id: int, daily_calories: int, weekly_calories: int):
    """Create a new goal for a user"""
    new_goal = Goal(
        user_id=user_id,
        daily_calories=daily_calories,
        weekly_calories=weekly_calories
    )
    session.add(new_goal)
    session.commit()
    return new_goal

def get_all_goals(session: Session, user_id: int):
    """Retrieve all goals for a user"""
    return session.query(Goal).filter_by(user_id=user_id).all()

def get_goal_by_id(session: Session, goal_id: int):
    """Retrieve a goal by its id"""
    return session.query(Goal).get(goal_id)

def update_goal(session: Session, goal_id: int, daily_calories: int = None, weekly_calories: int = None):
    """Update an existing goal"""
    goal = session.query(Goal).get(goal_id)
    if not goal:
        return None
    if daily_calories is not None:
        goal.daily_calories = daily_calories
    if weekly_calories is not None:
        goal.weekly_calories = weekly_calories
    session.commit()
    return goal

def delete_goal(session: Session, goal_id: int):
    """Delete a goal by its id"""
    goal = session.query(Goal).get(goal_id)
    if goal:
        session.delete(goal)
        session.commit()
        return True
    return False