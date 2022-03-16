from locust import User, task, between, wait_time

class MyUser(User):
    wait_time = between(5,15)

    @task
    def my_task(self):
        print("Its my first sample task")

    @task
    def my_task2(self):
        print("Its my first sample task")