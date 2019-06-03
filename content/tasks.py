from celery import task
import os

@task()
def sayHi():
    try:
        print('This greeting was ran from a distrubuted queue')
        return 'name is samus'
    except:
        print('No luck running task with celery')
    