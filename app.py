from flask import Flask, render_template, request, session
from textblob import TextBlob
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    sentiment_value = None
    
    # Initialize session history if it doesn't exist
    if 'history' not in session:
        session['history'] = []
    
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
        
        # Add to history (store timestamp, text, result, and sentiment value)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history_item = {
            'timestamp': timestamp,
            'text': text,
            'result': result,
            'sentiment_value': sentiment_value
        }
        
        # Add to the beginning of the list (most recent first)
        history = session['history']
        history.insert(0, history_item)
        
        # Keep only the 10 most recent entries
        if len(history) > 10:
            history = history[:10]
            
        session['history'] = history
    
    return render_template('index.html', result=result, sentiment_value=sentiment_value, 
                          active_page='home', history=session['history'])

@app.route('/about')
def about():
    return render_template('index.html', active_page='about')

@app.route('/clear-history')
def clear_history():
    if 'history' in session:
        session['history'] = []
    return render_template('index.html', active_page='home', history=[])

if __name__ == '__main__':
    app.run(debug=True) 