import nltk
import os

# Create directory if it doesn't exist
os.makedirs('./nltk_data', exist_ok=True)

# Download required NLTK data
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='./nltk_data')

print("NLTK data downloaded successfully.") 