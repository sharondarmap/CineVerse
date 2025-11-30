from infrastructure.memory_db import db_activities
from domain.activity.models import FilmActivity

class ActivityRepository:

    @staticmethod
    def save(activity: FilmActivity):
        db_activities[activity.activity_id] = activity
        return activity

    @staticmethod
    def get_by_id(activity_id: str):
        return db_activities.get(activity_id)

    @staticmethod
    def get_by_user(user_id: str):
        return [a for a in db_activities.values() if a.user_id == user_id]
