"""
Module for performance test cases
"""

import json
from locust import HttpUser, task


class PerformanceTests(HttpUser):
    """Test class for performance tests"""

    @task(1)
    def test_news_api(self):
        """A method to test performance of model inference API"""

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        sample = {"query": "Tesla", "num_articles": 2}
        self.client.post(
            "/news_articles", data=json.dumps(sample), headers=headers
        )
