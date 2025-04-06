# import sys
# from textblob import TextBlob

# print("Enter your review (Press Ctrl+D to stop on Linux/Mac or Ctrl+Z on Windows):")
# text = str(sys.stdin.read())
# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

# #print(sentiment)  # Output: 0.5 (positive)

# threshold=0
# if(sentiment > threshold):
#     print("Positive")
# elif(sentiment < threshold):
#     print("Negative")
# else:
#     print("Neutral")
