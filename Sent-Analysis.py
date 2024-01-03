import streamlit as st
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Generate Word Cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

st.title("Sentiment Analysis Web App")
user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze"):
    if user_input:  # Check if user input is not empty
        sentiment_score = analyze_sentiment(user_input)
        result = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
        st.success(f"Sentiment: {result}")
        
        # Generate and display Word Cloud
        generate_word_cloud(user_input)
    else:
        st.warning("Please enter some text for analysis.")
