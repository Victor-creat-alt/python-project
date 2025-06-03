from models import MealPlan, User

def test_meal_plan_creation(session):
    user = User(name="Meal User")
    session.add(user)
    session.commit()
    meal_plan = MealPlan(user_id=user.id, week_number=10, planned_meals="Oats, Chicken", nutrition_balance="High Protein")
    session.add(meal_plan)
    session.commit()
    assert meal_plan.id is not None
    assert meal_plan.week_number == 10
