import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/en/news")
        self.client.get("/en/services/web-application-development")