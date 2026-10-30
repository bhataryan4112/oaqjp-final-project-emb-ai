"""Verify Watson predictions for the five examples required by the assignment."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check each required dominant emotion using the live Watson service."""

    def test_joy(self):
        """A joyful statement should produce joy."""
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"], "joy"
        )

    def test_anger(self):
        """An angry statement should produce anger."""
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"], "anger"
        )

    def test_disgust(self):
        """A disgusted statement should produce disgust."""
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust",
        )

    def test_sadness(self):
        """A sad statement should produce sadness."""
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"], "sadness"
        )

    def test_fear(self):
        """A fearful statement should produce fear."""
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"],
            "fear",
        )


if __name__ == "__main__":
    unittest.main()
