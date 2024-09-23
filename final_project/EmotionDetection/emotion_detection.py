import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputt = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=inputt, headers=headers)
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, 
        "joy": None, "sadness": None, "dominant_emotion": None}
    formatted = json.loads(response.text)
    result = formatted["emotionPredictions"][0]["emotion"]
    dominant = 0
    dominant_emotion = ""
    for emotion in result:
        if result[emotion] > dominant:
            dominant = result[emotion]
            dominant_emotion = emotion
    result["dominant_emotion"] = dominant_emotion
    return result