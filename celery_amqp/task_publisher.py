from tasks import add
import time

# This is required to give RabbitMQ time to start-up
# otherwise celery will quit when trying to publish the task
# Docker recommends using some for of check-if-dependencies-started heuristic 
# but this is an easier hack for now
time.sleep(5)

while True:
    # Note how we call add as add.delay() - this means we're calling it asynchronously
    result = add.delay(2, 3)
    print("I've just published a new task with the unique taskID: {}", result)
    # Sleep for a bit before republishing
    time.sleep(3)
