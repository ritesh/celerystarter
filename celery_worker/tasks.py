from celery import Celery
import random
import time
app = Celery('tasks', backend='redis://redis', broker='pyamqp://guest@rabbit//')

@app.task
def add(x, y):
    #Fails some of the time
    if random.randint(0,3):
        time.sleep(3)
        return x + y
    else:
        raise ArithmeticError