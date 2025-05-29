from models.Report import Report
from sqlalchemy.orm import Session
from datetime import datetime

def create_report(session: Session, user_id: int, weekly_progress: float, goal_status: bool, total_calories: int, date: str):
    """Create a report for a user"""
    date_obj = datetime.fromisoformat(date)
    report = Report(
        user_id=user_id,
        weekly_progress=weekly_progress,
        goal_status=goal_status,
        total_calories=total_calories,
        date=date_obj
    )
    session.add(report)
    session.commit()
    return report

def get_all_reports(session: Session, user_id: int):
    """Get all reports for a user"""
    return session.query(Report).filter_by(user_id=user_id).all()

def get_report_by_id(session: Session, report_id: int):
    """Get a report by its id"""
    return session.query(Report).get(report_id)

def update_report(session: Session, report_id: int, weekly_progress: float = None, goal_status: bool = None, total_calories: int = None, date: str = None):
    """Update a report by id"""
    report = session.query(Report).get(report_id)
    if not report:
        return None
    if weekly_progress is not None:
        report.weekly_progress = weekly_progress
    if goal_status is not None:
        report.goal_status = goal_status
    if total_calories is not None:
        report.total_calories = total_calories
    if date is not None:
        report.date = datetime.fromisoformat(date)
    session.commit()
    return report

def delete_report(session: Session, report_id: int):
    """Delete a report by ID"""
    report = session.query(Report).get(report_id)
    if report:
        session.delete(report)
        session.commit()
        return True
    return False