import os
from flask import Flask, render_template, request
import nltk
from textblob import TextBlob

# Initialize NLTK data
nltk_data_dir = os.environ.get('NLTK_DATA', None)
if nltk_data_dir:
    nltk.data.path.append(nltk_data_dir)
try:
    # Try to make sure nltk data is available
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    # If not available, download it
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    sentiment_value = None
    
    if request.method == 'POST':
        text = request.form['text']
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
    
    return render_template('index.html', result=result, sentiment_value=sentiment_value, active_page='home')

@app.route('/about')
def about():
    return render_template('index.html', active_page='about')

# This is for local development
if __name__ == '__main__':
    app.run(debug=True)
    
# For serverless deployments
app = app 