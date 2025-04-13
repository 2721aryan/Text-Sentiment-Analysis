from flask import Flask, render_template, request, session
from textblob import TextBlob
from datetime import datetime
import os
from flask_session import Session

app = Flask(__name__)
# Secret key from environment variable with fallback
app.secret_key = os.environ.get('SECRET_KEY', 'text_sentiment_analysis_secret_key')

# Configure Flask-Session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_FILE_DIR"] = os.path.join(os.getcwd(), "flask_session")
Session(app)

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
    # Use PORT environment variable if available (for cloud deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 