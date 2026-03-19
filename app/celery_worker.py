from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks","app.delete_task"]   # IMPORTANT
)

from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "app.tasks.fetch_and_store_news",
        "schedule": crontab(minute="*"),
    },
    "delete-old-news-every-minute": {
        "task": "app.delete_task.delete_old_news",
        "schedule": crontab(minute="*"),
    },  
}

celery_app.conf.timezone = "UTC"