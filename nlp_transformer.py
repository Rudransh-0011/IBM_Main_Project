# nlp_transformer.py

from transformers import pipeline

# Load BERT for sentiment analysis
classifier = pipeline('sentiment-analysis')

# Example usage
if __name__ == "__main__":
    text = "This is the best product I've ever used!"
    result = classifier(text)
    print(result)