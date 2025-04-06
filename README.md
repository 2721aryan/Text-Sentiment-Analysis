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

2. Deploy to Vercel using one of these methods:
   
   **Option A: Deploy from GitHub**
   - Push your code to GitHub
   - Import the repository in the Vercel dashboard
   - Vercel will detect the configuration and deploy automatically
   
   **Option B: Deploy from CLI**
   ```
   vercel login
   vercel
   ```

3. **IMPORTANT: Troubleshooting Vercel Deployment**
   
   If you're still seeing 500 errors:
   - Use the "Preview" feature to understand the error
   - Check your function logs in the Vercel dashboard
   - Try deploying only the `/api` directory:
     ```
     vercel --cwd api
     ```
   - Consider pushing your entire project to GitHub and importing it in Vercel

### Alternative: Render.com Deployment (Recommended for Python)

1. Create a free account on [Render.com](https://render.com)
2. Choose "New Web Service" and connect your GitHub repository
3. Configure as a Python app with:
   - Build Command: `pip install -r requirements.txt && python download_nltk.py`
   - Start Command: `gunicorn app:app`
4. Deploy and your app will be live in minutes

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

## Usage

1. Enter text in the provided text area.
2. Click the "Analyze" button.
3. View the sentiment analysis result (Positive, Negative, or Neutral) and the sentiment score.

## About

The sentiment analysis is performed using TextBlob, which returns a polarity score between -1 (very negative) and 1 (very positive). A score of 0 is considered neutral. 