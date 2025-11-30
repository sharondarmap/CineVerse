from domain.activity.models import FilmActivity, LogEntry, Review
from domain.activity.repository import ActivityRepository
from uuid import uuid4

class ActivityService:

    @staticmethod
    def create(user_id: str, film_id: str):
        activity = FilmActivity.create(user_id, film_id)
        return ActivityRepository.save(activity)

    @staticmethod
    def add_log(activity, watched_date, rating):
        log = LogEntry(log_id=str(uuid4()), watched_date=watched_date, rating=rating)
        activity.logs.append(log)
        return ActivityRepository.save(activity)

    @staticmethod
    def add_review(activity, text, spoiler):
        review = Review(review_id=str(uuid4()), review_text=text, has_spoiler=spoiler)
        activity.review = review
        return ActivityRepository.save(activity)

    @staticmethod
    def get(activity_id: str):
        return ActivityRepository.get_by_id(activity_id)

    @staticmethod
    def list_user(user_id: str):
        return ActivityRepository.get_by_user(user_id)
