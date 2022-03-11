from locust import task, TaskSet, HttpUser, constant, SequentialTaskSet
#https://qa.hyperdrive.solutions/dex/auth/local/login?back=%2Fdex%2Fauth%3Fclient_id%3D0oa38lfy2q6kMWPCB4x7%26redirect_uri%3D%252Fauthservice%252Foidc%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%2Bgroups%26state%3DMTY0MzAyMzIyNHxOd3dBTkVKWE5qUlBTelZCTjFGWU4xUkpXRFpQTTFkR05GbFFVRE5LVlVkWlVUWk1XbE5JVVZwS1RqUkpUa2xGTnpkTFZsRkJSa0U9fPPcrSWiWl-jsUy7pJrkmf65so2pUY_JZZTlrpo9Eb6f&state=cu3oqk5l22o6xsxlk3i4x2ylu
#

class UserBehaviour(SequentialTaskSet):

    @task
    def login_post(self):
        self.client.post("/dex/auth/local/login?back:/dex/auth",{"login": "user@example.com", "password": "slX3MW5Q3hcKAxqqimfUcBxVb2GEuLjr"})
        print("Kuch to hua hain")

    @task
    def actualwork(self):
        print("Inside second task")


class User(HttpUser):
    host = "https://qa.hyperdrive.solutions"
    tasks = [UserBehaviour]
    wait_time = constant(1)