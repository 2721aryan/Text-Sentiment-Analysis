from http.server import BaseHTTPRequestHandler
from textblob import TextBlob
import json
import os
import urllib.parse
import nltk

# Ensure nltk data is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

# Read HTML template
with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'index.html'), 'r') as f:
    html_template = f.read()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the static HTML page
        try:
            public_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
            if self.path == '/':
                with open(os.path.join(public_dir, 'index.html'), 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Not found')
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())
        return
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = urllib.parse.parse_qs(post_data)
        
        text = form_data.get('text', [''])[0]
        result = None
        sentiment_value = None
        
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
            result = "Error analyzing text"
            sentiment_value = str(e)
        
        # Return JSON response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'result': result,
            'sentiment_value': sentiment_value
        }
        
        self.wfile.write(json.dumps(response).encode())
        return 