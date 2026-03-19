from app.database import SessionLocal
from app.model import News
import os
from celery import shared_task

@shared_task
def delete_old_news():
    db = SessionLocal()

    # we have to delete the rows every minute because the news api only returns the latest news and we want to keep our database clean
    db.query(News).filter(News.id%2==0).delete(synchronize_session=False)

    db.commit()
    db.close()

    return "News deleted successfully"