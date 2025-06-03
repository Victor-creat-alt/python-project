from models import Report, User

def test_report_creation(session):
    user = User(name="Report User")
    session.add(user)
    session.commit()
    report = Report(user_id=user.id, total_calories=1800, goal_status=True, weekly_progress=90.5)
    session.add(report)
    session.commit()
    assert report.id is not None
    assert report.total_calories == 1800