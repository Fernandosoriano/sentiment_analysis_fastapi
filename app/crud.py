from sqlalchemy.orm import Session
from app import models

def create_sentiment(db: Session, text: str, sentiment: str):
    try:
        sentiment_entry = models.Sentiment(text=text, sentiment=sentiment)
        db.add(sentiment_entry)
        db.commit()
        db.refresh(sentiment_entry)
        return sentiment_entry
    except Exception as e:
        print(f'The next error has occurred: {e}')

def get_sentiments(db: Session):
    try:
        return db.query(models.Sentiment).all()
    except Exception as e:
        print(f'The next error has occurred:{e}')

# Function to delete a specific sentiment by ID
def delete_sentiment_by_id(db: Session, sentiment_id: int):
    try:
        sentiment = db.query(models.Sentiment).filter(models.Sentiment.id == sentiment_id).first()
        if sentiment:
            db.delete(sentiment)
            db.commit()
            return True
        return False
    except Exception as e:
        print(f'The following error has ocurred: {e}')

# Function to delete all sentiments (optional)
def delete_all_sentiments(db: Session):
    try:
        db.query(models.Sentiment).delete()
        db.commit()
        return True
    except Exception as e:
        print(f'The following error has occurred:{e}')
