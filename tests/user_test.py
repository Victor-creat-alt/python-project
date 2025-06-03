from models import User

def test_user_creation(session):
    user = User(name="John Doe")
    session.add(user)
    session.commit()
    assert user.id is not None
    assert user.name == "John Doe"