import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.User import User
from models.FoodEntry import FoodEntry
from models.Goal import Goal
from models.Report import Report
from models.MealPlan import MealPlan
from typing import Optional
from datetime import datetime
from sqlalchemy import extract

app = typer.Typer()
DATABASE_URL = "postgresql://victor:victor123@localhost:5432/healthtracker"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Ensure that the tables exist
Base.metadata.create_all(engine)

def get_by_id(session, model, id):
    return session.get(model, id)

# USER COMMANDS
@app.command()
def user_create(name: str):
    session = Session()
    user = User(name=name)
    session.add(user)
    session.commit()
    typer.echo(f"User {name} created with ID {user.id}")
    session.close()

@app.command()
def user_list():
    session = Session()
    users = session.query(User).all()
    for user in users:
        typer.echo(f"User ID: {user.id}, Name: {user.name}")
    session.close()

@app.command()
def user_update(id: int, name: Optional[str] = None):
    session = Session()
    user = get_by_id(session, User, id)
    if not user:
        typer.echo(f"User with ID {id} not found.")
        session.close()
        return
    if name:
        user.name = name
        session.commit()
        typer.echo(f"User with ID {id} updated successfully to name '{name}'.")
    else:
        typer.echo("No new name provided. Nothing to update.")
    session.close()

@app.command()
def user_delete(id: int):
    session = Session()
    user = get_by_id(session, User, id)
    if not user:
        typer.echo(f"User with ID {id} not found.")
        session.close()
        return
    session.delete(user)
    session.commit()
    typer.echo(f"User with ID {id} deleted successfully.")
    session.close()

# FOOD ENTRY COMMANDS
@app.command()
def food_entry_create(
    user_id: int,
    food_name: str,
    calories: int,
    meal_type: str,
    quantity: int,
    date: str
):
    session = Session()
    try:
        date_obj = datetime.fromisoformat(date)
    except ValueError:
        typer.echo("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
        session.close()
        return
    food_entry = FoodEntry(
        user_id=user_id,
        food_name=food_name,
        calories=calories,
        meal_type=meal_type,
        quantity=quantity,
        date=date_obj
    )
    session.add(food_entry)
    session.commit()
    typer.echo(f"Food entry created for User ID {user_id}: {food_name}")
    session.close()

@app.command()
def food_entry_list(user_id: int):
    session = Session()
    food_entries = session.query(FoodEntry).filter_by(user_id=user_id).all()
    for entry in food_entries:
        typer.echo(
            f"Food Entry ID: {entry.id}, Food Name: {entry.food_name}, Calories: {entry.calories}, "
            f"Date: {entry.date}, Meal Type: {entry.meal_type}, Quantity: {entry.quantity}"
        )
    session.close()

@app.command()
def entry_update(
    id: int,
    food_name: Optional[str] = None,
    calories: Optional[int] = None,
    date: Optional[str] = None,
    meal_type: Optional[str] = None,
    quantity: Optional[int] = None
):
    session = Session()
    entry = get_by_id(session, FoodEntry, id)
    if not entry:
        typer.echo(f"Food entry with ID {id} not found.")
        session.close()
        return
    if food_name:
        entry.food_name = food_name
    if calories:
        entry.calories = calories
    if meal_type:
        entry.meal_type = meal_type
    if quantity:
        entry.quantity = quantity
    if date:
        try:
            entry.date = datetime.fromisoformat(date)
        except ValueError:
            typer.echo("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
            session.close()
            return
    session.commit()
    typer.echo(f"Food entry with ID {id} updated successfully.")
    session.close()

@app.command()
def entry_delete(id: int):
    session = Session()
    entry = get_by_id(session, FoodEntry, id)
    if not entry:
        typer.echo(f"Food entry with ID {id} not found.")
        session.close()
        return
    session.delete(entry)
    session.commit()
    typer.echo(f"Food Entry with ID {id} deleted successfully.")
    session.close()

# GOAL COMMANDS
@app.command()
def goal_create(user_id: int, daily_calories: int, weekly_calories: int):
    session = Session()
    goal = Goal(user_id=user_id, daily_calories=daily_calories, weekly_calories=weekly_calories)
    session.add(goal)
    session.commit()
    typer.echo(f"Goal created for User ID {user_id} with target calories {daily_calories} daily and {weekly_calories} weekly")
    session.close()

@app.command()
def goal_list(user_id: int):
    session = Session()
    goals = session.query(Goal).filter_by(user_id=user_id).all()
    for goal in goals:
        typer.echo(f"Goal ID: {goal.id}, Target Calories: {goal.daily_calories} daily, {goal.weekly_calories} weekly")
    session.close()

@app.command()
def update_goal(id: int, daily_calories: Optional[int] = None, weekly_calories: Optional[int] = None):
    session = Session()
    goal = get_by_id(session, Goal, id)
    if not goal:
        typer.echo(f"Goal with ID {id} not found.")
        session.close()
        return
    if daily_calories is not None:
        goal.daily_calories = daily_calories
    if weekly_calories is not None:
        goal.weekly_calories = weekly_calories
    session.commit()
    typer.echo(f"Goal with ID {id} updated successfully")
    session.close()

@app.command()
def goal_delete(id: int):
    session = Session()
    goal = get_by_id(session, Goal, id)
    if not goal:
        typer.echo(f"Goal with ID {id} not found.")
        session.close()
        return
    session.delete(goal)
    session.commit()
    typer.echo(f"Goal with ID {id} deleted successfully")
    session.close()

# REPORT COMMANDS
@app.command()
def report_generate(
    user_id: int,
    date: str
):
    """
    Generate a report for a user for the week containing the given date.
    Calculates total calories, weekly progress, and goal status automatically.
    """
    session = Session()
    user = get_by_id(session, User, user_id)
    if not user:
        typer.echo(f"User with ID {user_id} not found.")
        session.close()
        return

    try:
        date_obj = datetime.fromisoformat(date)
    except ValueError:
        typer.echo("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
        session.close()
        return

    # Get the week number and year for the given date
    week_number = date_obj.isocalendar()[1]
    year = date_obj.year

    # Sum all food entries for the user for that week (calories * quantity)
    food_entries = session.query(FoodEntry).filter(
        FoodEntry.user_id == user_id,
        extract('week', FoodEntry.date) == week_number,
        extract('year', FoodEntry.date) == year
    ).all()
    total_calories = sum(entry.calories * entry.quantity for entry in food_entries)

    # Get the user's goal
    goal = session.query(Goal).filter_by(user_id=user_id).order_by(Goal.created_at.desc()).first()
    if not goal:
        typer.echo("No goal set for this user.")
        session.close()
        return

    # Calculate weekly progress and goal status
    weekly_progress = total_calories / goal.weekly_calories if goal.weekly_calories else 0
    goal_status = total_calories <= goal.weekly_calories

    report = Report(
        user_id=user_id,
        total_calories=total_calories,
        date=date_obj,
        goal_status=goal_status,
        weekly_progress=weekly_progress
    )
    session.add(report)
    session.commit()
    typer.echo(
        f"Report generated for User ID {user_id}: Total Calories {total_calories}, "
        f"Weekly Progress: {weekly_progress:.2f}, Goal Status: {'Met' if goal_status else 'Not Met'}"
    )
    session.close()
       
@app.command()
def report_list(user_id: int):
    session = Session()
    reports = session.query(Report).filter_by(user_id=user_id).all()
    for report in reports:
        typer.echo(
            f"Report ID: {report.id} Total Calories: {report.total_calories} Date: {report.date}, "
            f"Goal Status: {report.goal_status}, Weekly Progress: {report.weekly_progress}"
        )
    session.close()

@app.command()
def update_report(
    id: int,
    total_calories: Optional[int] = None,
    goal_status: Optional[bool] = None,
    weekly_progress: Optional[float] = None,
    date: Optional[str] = None
):
    session = Session()
    report = get_by_id(session, Report, id)
    if not report:
        typer.echo(f"Report with ID {id} not found.")
        session.close()
        return
    if date:
        try:
            report.date = datetime.fromisoformat(date)
        except ValueError:
            typer.echo("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
            session.close()
            return
    if weekly_progress is not None:
        report.weekly_progress = weekly_progress
    if total_calories is not None:
        report.total_calories = total_calories
    if goal_status is not None:
        report.goal_status = goal_status
    session.commit()
    typer.echo(f"Report with ID {id} updated successfully")
    session.close()

@app.command()
def delete_report(id: int):
    session = Session()
    report = get_by_id(session, Report, id)
    if not report:
        typer.echo(f"Report with ID {id} not found.")
        session.close()
        return
    session.delete(report)
    session.commit()
    typer.echo(f"Report with ID {id} deleted successfully")
    session.close()

# MEAL PLAN COMMANDS
@app.command()
def meal_plan_create(
    user_id: int,
    week_number: int,
    day_of_week: str,
    meal_type: str,
    planned_meals: str,
    nutrition_balance: str
):
    """
    Generate a meal plan for a user for a specific day and meal type in the week.
    """
    session = Session()
    meal_plan = MealPlan(
        user_id=user_id,
        week_number=week_number,
        day_of_week=day_of_week,
        meal_type=meal_type,
        planned_meals=planned_meals,
        nutrition_balance=nutrition_balance
    )
    session.add(meal_plan)
    session.commit()
    typer.echo(f"Meal plan created for User ID {user_id} for {day_of_week} ({meal_type}) in week {week_number}")
    session.close()

@app.command()
def meal_plan_list(user_id: int, week_number: Optional[int] = None, day_of_week: Optional[str] = None, meal_type: Optional[str] = None):
    """
    List all meal plans for a User, optionally filtered by week, day, or meal type.
    """
    session = Session()
    query = session.query(MealPlan).filter_by(user_id=user_id)
    if week_number is not None:
        query = query.filter_by(week_number=week_number)
    if day_of_week is not None:
        query = query.filter_by(day_of_week=day_of_week)
    if meal_type is not None:
        query = query.filter_by(meal_type=meal_type)
    meal_plans = query.all()
    for meal_plan in meal_plans:
        typer.echo(
            f"Meal Plan ID: {meal_plan.id}, Week: {meal_plan.week_number}, Day: {meal_plan.day_of_week}, "
            f"Meal Type: {meal_plan.meal_type}, Planned Meals: {meal_plan.planned_meals}, Nutrition Balance: {meal_plan.nutrition_balance}"
        )
    session.close()

@app.command()
def update_meal_plan(
    id: int,
    week_number: Optional[int] = None,
    day_of_week: Optional[str] = None,
    meal_type: Optional[str] = None,
    planned_meals: Optional[str] = None,
    nutrition_balance: Optional[str] = None
):
    """
    Update a meal plan.
    """
    session = Session()
    meal_plan = get_by_id(session, MealPlan, id)
    if not meal_plan:
        typer.echo(f"Meal Plan with ID {id} not found.")
        session.close()
        return
    if week_number is not None:
        meal_plan.week_number = week_number
    if day_of_week is not None:
        meal_plan.day_of_week = day_of_week
    if meal_type is not None:
        meal_plan.meal_type = meal_type
    if planned_meals is not None:
        meal_plan.planned_meals = planned_meals
    if nutrition_balance is not None:
        meal_plan.nutrition_balance = nutrition_balance
    session.commit()
    typer.echo(f"Meal Plan with ID {id} updated successfully.")
    session.close()

@app.command()
def delete_meal_plan(id: int):
    session = Session()
    meal_plan = get_by_id(session, MealPlan, id)
    if not meal_plan:
        typer.echo(f"Meal plan with ID {id} not found.")
        session.close()
        return
    session.delete(meal_plan)
    session.commit()
    typer.echo(f"Meal Plan with ID {id} deleted successfully.")
    session.close()

# ...existing code...

@app.command()
def meal_plan_share(meal_plan_id: int, user_id: int):
    """
    Share a meal plan with another user (adds to meal_users).
    This will populate the meal_users association table.
    """
    session = Session()
    meal_plan = get_by_id(session, MealPlan, meal_plan_id)
    user = get_by_id(session, User, user_id)
    if not meal_plan:
        typer.echo(f"Meal plan with ID {meal_plan_id} not found.")
        session.close()
        return
    if not user:
        typer.echo(f"User with ID {user_id} not found.")
        session.close()
        return
    if user in meal_plan.shared_users:
        typer.echo(f"User {user_id} already has access to meal plan {meal_plan_id}.")
        session.close()
        return
    meal_plan.shared_users.append(user)
    session.commit()
    typer.echo(f"Meal plan {meal_plan_id} shared with user {user_id}.")
    session.close()

@app.command()
def meal_plan_shared_users(meal_plan_id: int):
    """
    List all users a meal plan is shared with.
    """
    session = Session()
    meal_plan = get_by_id(session, MealPlan, meal_plan_id)
    if not meal_plan:
        typer.echo(f"Meal plan with ID {meal_plan_id} not found.")
        session.close()
        return
    if not meal_plan.shared_users:
        typer.echo("No users have access to this meal plan.")
    else:
        for user in meal_plan.shared_users:
            typer.echo(f"User ID: {user.id}, Name: {user.name}")
    session.close()

@app.command()
def user_shared_meal_plans(user_id: int):
    """
    List all meal plans shared with a user.
    """
    session = Session()
    user = get_by_id(session, User, user_id)
    if not user:
        typer.echo(f"User with ID {user_id} not found.")
        session.close()
        return
    if not hasattr(user, "shared_meal_plans") or not user.shared_meal_plans:
        typer.echo("No meal plans shared with this user.")
    else:
        for meal_plan in user.shared_meal_plans:
            typer.echo(
                f"Meal Plan ID: {meal_plan.id}, Week: {meal_plan.week_number}, Day: {meal_plan.day_of_week}, "
                f"Meal Type: {meal_plan.meal_type}, Planned Meals: {meal_plan.planned_meals}, Nutrition Balance: {meal_plan.nutrition_balance}"
            )
    session.close()
# ...existing code...

if __name__ == "__main__":
    app()