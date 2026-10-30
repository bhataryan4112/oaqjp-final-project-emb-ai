# Final Project

## Project name: Emotion Detector

A Flask web application that uses IBM Watson NLP to detect anger, disgust,
fear, joy, and sadness in English text and report the dominant emotion.

### Run

```sh
python3 -m pip install -r requirements.txt
python3 server.py
```

Open http://localhost:5000 in a browser.

### Test and analyze

```sh
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
python3 test_emotion_detection.py
python3 -m pylint server.py
```

The detector and the five prediction tests need access to the IBM Watson
service provided by the Skills Network lab. No local substitute generates
emotion scores. HTTP 400 responses return all six output keys with None values.
The web interface rejects blank input with "Invalid text! Please try again!".
