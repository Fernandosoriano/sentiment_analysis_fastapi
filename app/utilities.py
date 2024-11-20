
def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of a given text and returns 'positive', 'negative', or 'neutral'.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"