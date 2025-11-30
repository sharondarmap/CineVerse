from fastapi import APIRouter, Depends, HTTPException
from application.activity_service import ActivityService
from domain.activity.schemas import ActivityCreate, LogCreate, ReviewCreate
from api.dependencies import get_current_user

router = APIRouter(prefix="/activity", tags=["Activity"])

@router.post("")
def create_activity(data: ActivityCreate, current_user=Depends(get_current_user)):
    return ActivityService.create(data.user_id, data.film_id)

@router.post("/{activity_id}/log")
def add_log(activity_id: str, data: LogCreate, current_user=Depends(get_current_user)):
    activity = ActivityService.get(activity_id)
    if not activity:
        raise HTTPException(404, "Activity not found")
    return ActivityService.add_log(activity, data.watched_date, data.rating)

@router.post("/{activity_id}/review")
def add_review(activity_id: str, data: ReviewCreate, current_user=Depends(get_current_user)):
    activity = ActivityService.get(activity_id)
    if not activity:
        raise HTTPException(404, "Activity not found")
    return ActivityService.add_review(activity, data.review_text, data.has_spoiler)

@router.get("/user/{user_id}")
def list_user_activities(user_id: str):
    return ActivityService.list_user(user_id)
