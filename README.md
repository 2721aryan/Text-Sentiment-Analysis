# Text Sentiment Analysis Web Application

A simple web application that analyzes the sentiment of text input using TextBlob.

## Local Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Download required NLTK data for TextBlob:
   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

## Running the Application Locally

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Deployment Options

### Vercel Deployment

1. Make sure you have the Vercel CLI installed:
   ```
   npm install -g vercel
   ```

2. Deploy to Vercel:
   ```
   vercel login
   vercel
   ```

3. Troubleshooting Vercel Deployment:
   - If you encounter 500 errors, check the Vercel logs in your dashboard
   - Ensure NLTK data is properly downloaded by the build process
   - The files `vercel.json`, `requirements-vercel.txt`, and `nltk.txt` are specifically for Vercel deployment

### Heroku Deployment

1. Create a `Procfile` in the project root:
   ```
   web: gunicorn app:app
   ```

2. Add `gunicorn` to `requirements.txt`

3. Deploy with Heroku CLI:
   ```
   heroku create
   git push heroku main
   ```

### Other Cloud Platforms

The application can be deployed to other platforms that support Python:

- **Google Cloud Run**: Build a container with a Dockerfile
- **AWS Lambda**: Use Zappa or AWS Chalice
- **Azure App Service**: Deploy directly from repository
- **Render.com**: Simple deployment with support for Python web services

## Usage

1. Enter text in the provided text area.
2. Click the "Analyze" button.
3. View the sentiment analysis result (Positive, Negative, or Neutral) and the sentiment score.

## About

The sentiment analysis is performed using TextBlob, which returns a polarity score between -1 (very negative) and 1 (very positive). A score of 0 is considered neutral. 