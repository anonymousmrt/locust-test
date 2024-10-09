import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def hello_world(self):
        # self.client.get("/dashboard")
        self.client.get("/")
        self.client.get("/en/news")
        self.client.get("/en/services/web-application-development")
    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"email":"tuyenvn@haposoft.com", "password":"passs"})