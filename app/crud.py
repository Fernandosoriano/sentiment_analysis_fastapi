from sqlalchemy.orm import Session
from app import models

def create_sentiment(db: Session, text: str, sentiment: str):
    sentiment_entry = models.Sentiment(text=text, sentiment=sentiment)
    db.add(sentiment_entry)
    db.commit()
    db.refresh(sentiment_entry)
    return sentiment_entry

def get_sentiments(db: Session):
    return db.query(models.Sentiment).all()

# Function to delete a specific sentiment by ID
def delete_sentiment_by_id(db: Session, sentiment_id: int):
    sentiment = db.query(models.Sentiment).filter(models.Sentiment.id == sentiment_id).first()
    if sentiment:
        db.delete(sentiment)
        db.commit()
        return True
    return False

# Function to delete all sentiments (optional)
def delete_all_sentiments(db: Session):
    db.query(models.Sentiment).delete()
    db.commit()
    return True
