# Text Sentiment Analysis Web Application

A simple web application that analyzes the sentiment of text input using TextBlob.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Download required NLTK data for TextBlob:
   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

## Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Enter text in the provided text area.
2. Click the "Analyze" button.
3. View the sentiment analysis result (Positive, Negative, or Neutral) and the sentiment score.

## About

The sentiment analysis is performed using TextBlob, which returns a polarity score between -1 (very negative) and 1 (very positive). A score of 0 is considered neutral. 

## To watch how this works visit :

https://text-sentiment-analysis-55dp.onrender.com/
