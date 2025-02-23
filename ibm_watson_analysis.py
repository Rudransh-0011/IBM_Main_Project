# ibm_watson_analysis.py

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate and set up Watson NLU
authenticator = IAMAuthenticator('00KpLFBSEt9cS20-Br5qMjcozhJWclj5TaUglh0ibmTv')
nlu = NaturalLanguageUnderstandingV1(version='2023-03-15', authenticator=authenticator)
nlu.set_service_url('https://api.jp-tok.natural-language-understanding.watson.cloud.ibm.com/instances/a59e4161-27d5-42d1-ab3f-2d97d4b5a805')

# Analyze customer interaction text
def analyze_customer_interaction(text):
    response = nlu.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions(), entities=EntitiesOptions())
    ).get_result()
    return response

# Example usage
if __name__ == "__main__":
    text = "I love this product, but the delivery was late."
    analysis = analyze_customer_interaction(text)
    print("Sentiment:", analysis['sentiment']['document']['label'])
    print("Entities:", analysis['entities'])