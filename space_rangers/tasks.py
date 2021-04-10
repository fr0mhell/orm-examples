from celery import shared_task
from time import sleep


@shared_task
def dummy_progress(seconds: int):
    for i in range(seconds):
        sleep(1)
        print(f'Dummy progress: {i+1} / {seconds} sec')
