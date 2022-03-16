from locust import User, SequentialTaskSet, between, task

class SeqClass1(SequentialTaskSet):
    @task
    def myfirsttask(self):
        print("My 1st function from class 1")
    
    @task
    def mysecondttask(self):
        print("My 2nd function from class 1")

    @task
    def mythirdtask(self):
        print("My 3rd function from class 1")

    @task
    def myInterupt(self):
        self.interrupt()

class SeqClass2(SequentialTaskSet):
    @task
    @task
    def myfirsttask(self):
        print("My 1st function from class 2")
    
    @task
    def mysecondttask(self):
        print("My 2nd function from class 2")

    @task
    def mythirdtask(self):
        print("My 3rd function from class 2")
    @task
    def myInterupt(self):
        self.interrupt()

class MyUser(User):
    wait_time = between(2,3)
    tasks = {
        SeqClass1:5,
        SeqClass2:5
    
    }
