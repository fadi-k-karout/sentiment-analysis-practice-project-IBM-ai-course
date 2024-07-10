import requests
import json
def sentiment_analyzer(text_to_analyze: str) -> dict:
    '''This function takes a text as an input, sends a post api request to ibm-watson NlpService, returns label and score of document sentiment'''
    URL: str = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    HEADERS: dict = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj: dict = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers = HEADERS)
    formatted_response: dict = json.loads(response.text)
    docuemnt_sentiment: dict = formatted_response['documentSentiment']
    label_and_score: dict = {key:docuemnt_sentiment[key] for key in ['label', 'score'] if key in docuemnt_sentiment}
    return label_and_score