from flask import Flask, render_template, request
from textblob import TextBlob
import os
import sys
import importlib.util

# Add the parent directory to the path so we can access templates
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Flask app
app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    sentiment_value = None
    
    if request.method == 'POST':
        text = request.form['text']
        try:
            blob = TextBlob(text)
            sentiment = blob.sentiment.polarity
            sentiment_value = round(sentiment, 2)
            
            threshold = 0
            if sentiment > threshold:
                result = "Positive"
            elif sentiment < threshold:
                result = "Negative"
            else:
                result = "Neutral"
        except Exception as e:
            # Simple error handling
            result = "Error analyzing text"
            sentiment_value = str(e)
    
    return render_template('index.html', result=result, sentiment_value=sentiment_value, active_page='home')

@app.route('/about')
def about():
    return render_template('index.html', active_page='about')

# For Vercel serverless
def handler(request, context):
    with app.request_context(request):
        return app(request) 