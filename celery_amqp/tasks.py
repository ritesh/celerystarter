from celery import Celery
import random
app = Celery('tasks', backend='redis://redis', broker='pyamqp://guest@rabbit//')

@app.task
def add(x, y):
    # Same as the tasks.py in the worker
    # but you could leave this as a stub and it would still work
    # as long as you can import add
    if random.randint(0,3):
        return x + y
    else:
        raise ArithmeticError