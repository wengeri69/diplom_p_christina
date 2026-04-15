from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def create_post(self):
        payload = {
            'login:"ddklsfdsf@test.com"',
            'password: "gffdffggdfdf"'
        }
        self.client.post("/api/profile/login", json=payload)
# https://old.yummyani.me
# locust -f .\locustfile.py
