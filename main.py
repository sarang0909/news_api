"""A main script to run news api.

"""

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.utility.loggers import logger
from src.news_api import NewsAPIClient


class InputData(BaseModel):
    """A class to define data and it's type for input data.

    Args:
        BaseModel :  A base datatype class
    """

    query: str
    num_articles: int


app = FastAPI()
news_api_client = NewsAPIClient()


@app.get("/")
async def read_root():
    """basic server health check url

    Returns:
        dict : A message that server is running
    """

    logger.info("API server is running.")
    return {"msg": "API server is running"}


@app.post("/news_articles/")
async def get_news_articles(input_data: InputData):
    """A method to return articles on API request

    Args:
        input_data (InputData): Input data required for model

    Returns:
        dict : articles text
    """

    try:
        return {
            "news_api_output": news_api_client.get_articles(
                input_data.query, input_data.num_articles
            )
        }
    except Exception as error:
        message = "Error while creating output"
        logger.error(message, str(error))


# This is used only for unit testing the application/
# or for running this app as standalone instead of via docker
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
