from models import Goal, User

def test_goal_creation(session):
    user = User(name="Goal User")
    session.add(user)
    session.commit()
    goal = Goal(user_id=user.id, daily_calories=2000, weekly_calories=14000)
    session.add(goal)
    session.commit()
    assert goal.id is not None
    assert goal.daily_calories == 2000
