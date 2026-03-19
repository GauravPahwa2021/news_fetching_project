from app.database import SessionLocal
from app.model import News
import requests
import os
from dotenv import load_dotenv
from celery import shared_task


load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

@shared_task
def fetch_and_store_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
    except Exception as e:
        print("Error fetching news:", e)
        return "Failed"

    db = SessionLocal()

    for article in data.get("articles", []):
        news = News(
            title=article.get("title"),
            description=article.get("description"),
            url=article.get("url")
        )
        db.add(news)

    db.commit()
    db.close()

    return "News stored successfully"