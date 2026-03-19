from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    url = Column(String(255))