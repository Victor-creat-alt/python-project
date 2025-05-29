from models.User import User
from sqlalchemy.orm import Session

def create_user(session: Session, name: str):
    """Create a new user with a given name"""
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    return new_user

def get_all_users(session: Session):
    """Retrieve all users from the database"""
    return session.query(User).all()

def get_user_by_id(session: Session, user_id: int):
    """Retrieve a user by their id"""
    return session.query(User).get(user_id)

def delete_user(session: Session, user_id: int):
    """Delete a user by their id"""
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False