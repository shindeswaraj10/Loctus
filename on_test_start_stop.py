from locust import User, SequentialTaskSet, between, events, task, wait_time


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("************Exeution Started************")

@events.test_stop.add_listener
def on_test_stop(**lwargs):
    print("************Exeution Started************")

class SearchProduct(SequentialTaskSet):
    
    @task
    def myFirstTask(self):
        print("my 1st task")
    
    @task
    def mySecondTask(self):
        print("my 2nd task")
    
    @task
    def myThirdTask(self):
        print("my 3rd task")

class MyMan(User):
    wait_time = between(1,2)
    tasks = [SearchProduct]

    def on_start(self):
        print("Run once for each User Created")

    def on_stop(self):
        print("Run once for each User is Stoped")

