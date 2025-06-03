from models import FoodEntry, User

def test_food_entry_creation(session):
    user = User(name="Jane Doe")
    session.add(user)
    session.commit()
    food_entry = FoodEntry(
        user_id=user.id,
        food_name="Apple",
        calories=95,
        meal_type="Breakfast",
        quantity=1
    )
    session.add(food_entry)
    session.commit()
    assert food_entry.id is not None
    assert food_entry.food_name == "Apple"
