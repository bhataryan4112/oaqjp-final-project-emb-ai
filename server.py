"""Serve the Watson NLP emotion detector through Flask.

Run static analysis with: python3 -m pylint server.py
"""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
INVALID_INPUT = "Invalid text! Please try again!"


@app.route("/")
def index():
    """Render the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Return the five scores and dominant emotion, or an input error."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return INVALID_INPUT
    try:
        result = emotion_detector(text_to_analyze)
    except RequestException:
        return "Emotion detection service is unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return INVALID_INPUT
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
