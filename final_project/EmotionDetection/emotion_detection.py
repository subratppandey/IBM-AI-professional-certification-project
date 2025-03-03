import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = payload, headers = headers)
    res = json.loads(response.text)
    formatted_response = res['emotionPredictions'][0]['emotion']
    dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
    formatted_response['dominant_emotion'] = dominant_emotion
    return formatted_response 