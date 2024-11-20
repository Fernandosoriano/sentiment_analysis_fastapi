from sqlalchemy.orm import Session
from app import models, schemas

def create_sentiment(db: Session, sentiment_data: schemas.SentimentCreate, sentiment_value: str):
    new_sentiment = models.Sentiment(
        text=sentiment_data.text,
        sentiment=sentiment_value
    )
    db.add(new_sentiment)
    db.commit()
    db.refresh(new_sentiment)
    return new_sentiment

def get_sentiments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sentiment).offset(skip).limit(limit).all()
