'''This module include the functionality
    to do sentiment analysis'''

import json
import requests

def sentiment_analyzer(text_to_analyze: str) -> dict | None:
    '''This function takes a text as an input, 
       sends a post api request to ibm-watson NlpService,
       returns label and score of document sentiment'''

    if not isinstance(text_to_analyze, str) or text_to_analyze.strip() == "":
        return None

    url: str = ("https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1"
                + "/NlpService/SentimentPredict")
    headers: dict = {"grpc-metadata-mm-model-id":
                     "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    document: dict = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = document, headers = headers, timeout = 60)

    if response.status_code == 500:
        return None

    formatted_response: dict = json.loads(response.text)
    docuemnt_sentiment: dict = formatted_response['documentSentiment']
    label_and_score: dict = {key:docuemnt_sentiment[key] for key in ['label', 'score']
                             if key in docuemnt_sentiment}
    return label_and_score
