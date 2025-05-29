from models.MealPlan import MealPlan
from sqlalchemy.orm import Session

def create_meal_plan(session: Session, user_id: int, week_number: int, planned_meals: str, nutrition_balance: str):
    """Create a new meal plan for a user"""
    meal_plan = MealPlan(
        user_id=user_id,
        week_number=week_number,
        planned_meals=planned_meals,
        nutrition_balance=nutrition_balance
    )
    session.add(meal_plan)
    session.commit()
    return meal_plan

def get_meal_plans_by_user(session: Session, user_id: int):
    """Retrieve all meal plans for a user"""
    return session.query(MealPlan).filter_by(user_id=user_id).all()

def get_meal_plan_by_id(session: Session, meal_plan_id: int):
    """Retrieve a meal plan by its id"""
    return session.query(MealPlan).get(meal_plan_id)

def update_meal_plan(session: Session, meal_plan_id: int, week_number: int = None, planned_meals: str = None, nutrition_balance: str = None):
    """Update an existing meal plan"""
    meal_plan = session.query(MealPlan).get(meal_plan_id)
    if not meal_plan:
        return None
    if week_number is not None:
        meal_plan.week_number = week_number
    if planned_meals is not None:
        meal_plan.planned_meals = planned_meals
    if nutrition_balance is not None:
        meal_plan.nutrition_balance = nutrition_balance
    session.commit()
    return meal_plan

def delete_meal_plan(session: Session, meal_plan_id: int):
    """Delete a meal plan by its id"""
    meal_plan = session.query(MealPlan).get(meal_plan_id)
    if meal_plan:
        session.delete(meal_plan)
        session.commit()
        return True
    return False