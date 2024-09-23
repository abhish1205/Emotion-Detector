"""
This module contains a Flask app that provides an emotion detection service.
The app defines two routes: one for serving the homepage and one for processing text 
and returning emotion scores and the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    ''' This function calls the application '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': "
            f"{response['joy']} and 'sadness': {response['sadness']}. The dominant "
            f"emotion is {response['dominant_emotion']}."
        )

    return response_text

@app.route("/")
def render_index_page():
    ''' This is the function to render the index page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
