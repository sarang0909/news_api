"""
Module for functional test cases of news api code.
"""

from src.news_api import NewsAPIClient


class TestPredictor:
    """Test class for unit test cases of NewsAPIClient."""

    def test_model_output(self):
        """Tests model output."""

        assert isinstance(NewsAPIClient().get_articles("Tesla", 1), str)
