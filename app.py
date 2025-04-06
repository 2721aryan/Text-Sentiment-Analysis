from flask import Flask, render_template, request
from textblob import TextBlob

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