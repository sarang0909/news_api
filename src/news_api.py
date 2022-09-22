"""A News API module to get news articles.

"""

import pandas as pd
from newsapi import NewsApiClient
from newspaper import Article


from src.utility import constants
from src.utility.loggers import logger
from src.utility.utils import config


class NewsAPIClient:
    """
    This is a class for news api.

    Attributes:
        __client : The news api library client
    """

    __client = None

    def __init__(self):
        """Private constructor"""

        self.__client = NewsApiClient(
            api_key=config.get(constants.NEWS_API_KEY)
        )

    def get_client(self):
        """A method to get the news api client

        Returns:
            __client : NewsApiClient class instance
        """

        if self.__client is None:
            self.__client = NewsApiClient(
                api_key=config.get(constants.NEWS_API_KEY)
            )
        return self.__client

    def get_news(self, entity, num_articles=5):
        """A method to get news data

        Args:
            entity (str): A query to fetch news articles
            num_articles (int, optional): Number of news articles. Defaults to 5.

        Returns:
            artciles(json): Articles with their metadata
        """

        all_data = self.__client.get_everything(
            q=entity,
            sources=config.get(constants.NEWS_SOURCES),
            language=config.get(constants.LANGUAGE),
            page_size=num_articles,
        )

        return all_data["articles"]

    def get_article_text(self, url):
        """A method to get complete news article text

        Args:
            url (str): URL to article

        Returns:
            text(str): An article text
        """

        try:
            article = Article(url)
            article.download()
            article.parse()
        except Exception as error:
            message = "Error while fetching article text"
            logger.error(message, str(error))
            return ""
        return article.text

    def get_articles(self, entity, num_articles=5):
        """A method to get article texts

        Args:
            entity (str): A query to fetch news articles
            num_articles (int, optional): Number of news articles. Defaults to 5.

        Returns:
            artciles(json): Articles text
        """

        news_articles = self.get_news(entity, num_articles)
        articles = pd.DataFrame.from_records(news_articles)
        articles["article_text"] = articles.apply(
            lambda row: self.get_article_text(row["url"]), axis=1
        )
        return articles["article_text"].to_json()
