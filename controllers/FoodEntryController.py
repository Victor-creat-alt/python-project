from models.FoodEntry import FoodEntry
from sqlalchemy.orm import Session
from datetime import datetime

def create_food_entry(session: Session, user_id: int, food_name: str, calories: int, meal_type: str, quantity: int, date: str):
    """Create a new food entry for a user"""
    date_obj = datetime.fromisoformat(date)
    new_entry = FoodEntry(
        user_id=user_id,
        food_name=food_name,
        calories=calories,
        meal_type=meal_type,
        quantity=quantity,
        date=date_obj
    )
    session.add(new_entry)
    session.commit()
    return new_entry

def get_all_food_entries(session: Session, user_id: int):
    """Retrieve all food entries for a user"""
    return session.query(FoodEntry).filter_by(user_id=user_id).all()

def get_food_entry_by_id(session: Session, entry_id: int):
    """Retrieve a food entry by its id"""
    return session.query(FoodEntry).get(entry_id)

def update_food_entry(session: Session, entry_id: int, food_name: str = None, calories: int = None, meal_type: str = None, quantity: int = None, date: str = None):
    """Update an existing food entry"""
    entry = session.query(FoodEntry).get(entry_id)
    if not entry:
        return None
    if food_name is not None:
        entry.food_name = food_name
    if calories is not None:
        entry.calories = calories
    if meal_type is not None:
        entry.meal_type = meal_type
    if quantity is not None:
        entry.quantity = quantity
    if date is not None:
        entry.date = datetime.fromisoformat(date)
    session.commit()
    return entry

def delete_food_entry(session: Session, entry_id: int):
    """Delete a food entry by its id"""
    entry = session.query(FoodEntry).get(entry_id)
    if entry:
        session.delete(entry)
        session.commit()
        return True
    return False