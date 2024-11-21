from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from typing import List
from app.utilities import analyze_sentiment

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/analyze_sentiment/")
def analyze_multiple_sentiments(comments: List[str], db: Session = Depends(get_db)):
    sentiments = []
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        crud.create_sentiment(db, comment, sentiment)
        
        sentiments.append({"comment": comment, "sentiment": sentiment})
    
    positive_count = sum(1 for s in sentiments if s["sentiment"] == "positive")
    negative_count = sum(1 for s in sentiments if s["sentiment"] == "negative")
    neutral_count = sum(1 for s in sentiments if s["sentiment"] == "neutral")
    
    overall_sentiment = "neutral" 
    if positive_count > negative_count:
        overall_sentiment = "positive"
    elif negative_count > positive_count:
        overall_sentiment = "negative"
    
    return {
        "overall_sentiment": overall_sentiment,
        "details": {
            "positive_count": positive_count,
            "negative_count": negative_count,
            "neutral_count": neutral_count
        }
    }

@app.get("/sentiments/", response_model=list[schemas.Sentiment])
def read_sentiments(db: Session = Depends(get_db)):
    return crud.get_sentiments(db)
