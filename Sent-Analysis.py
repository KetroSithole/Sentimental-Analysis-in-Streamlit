import streamlit as st
from textblob import TextBlob

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

st.title("Sentiment Analysis Web App")
user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze"):
    if user_input:  # Check if user input is not empty
        result = analyze_sentiment(user_input)
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text for analysis.")
