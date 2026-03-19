from fastapi import FastAPI, Depends
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from app.model import News

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "News API with Celery is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/news")
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()