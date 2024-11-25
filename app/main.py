from fastapi import FastAPI, Depends, HTTPException
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
    except Exception as e:
        print(f'The following error has occurred: {e}')
    finally:
        db.close()

app = FastAPI()

@app.post("/analyze_sentiment/")
def analyze_multiple_sentiments(comments: List[str], db: Session = Depends(get_db)):
    try:
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
    except Exception as e:
        print(f'The following error has occurred: {e}')

@app.get("/sentiments/", response_model=list[schemas.Sentiment])
def read_sentiments(db: Session = Depends(get_db)):
    try:
        return crud.get_sentiments(db)
    except Exception as e:
        print(f'The following error has occurred:{e}')

# DELETE route to delete a specific sentiment by ID
@app.delete("/sentiments/{sentiment_id}")
def delete_sentiment(sentiment_id: int, db: Session = Depends(get_db)):
    try:
        success = crud.delete_sentiment_by_id(db, sentiment_id)
        if not success:
            raise HTTPException(status_code=404, detail="Sentiment not found")
        return {"detail": "Sentiment deleted successfully"}
    except Exception as e:
        print(f'The following error has occurred: {e}')

# DELETE route to delete all sentiments
@app.delete("/sentiments/")
def delete_all_sentiments(db: Session = Depends(get_db)):
    try:
        crud.delete_all_sentiments(db)
        return {"detail": "All sentiments deleted successfully"}
    except Exception as e:
        print(f'The following error has ocurred:{e}')
