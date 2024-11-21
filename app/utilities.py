from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of a given text and returns 'positive', 'negative', or 'neutral'.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # debugging to define the range of sentiment analysis:
    # print(f"Text: {text}\nPolarity: {polarity}")

    if -0.2 <= polarity <= 0.2:
        return "neutral"
    elif polarity > 0.2:
        return "positive"
    else:
        return "negative"

