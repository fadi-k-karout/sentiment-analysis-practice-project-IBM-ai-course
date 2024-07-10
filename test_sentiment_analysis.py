from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        positive_sentiment: dict = sentiment_analyzer("I love working with Python")
        self.assertEqual(positive_sentiment['label'], "SENT_POSITIVE")
        negative_sentiment: dict = sentiment_analyzer("I hate working with Pyhton")
        self.assertEqual(negative_sentiment['label'], "SENT_NEGATIVE")
        neutral_sentiment: dict = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(neutral_sentiment['label'], "SENT_NEUTRAL")
        
unittest.main()