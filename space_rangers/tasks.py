import logging

from celery import shared_task
from time import sleep

logger = logging.getLogger('django')


@shared_task(bind=True)
def dummy_progress(self, seconds: int):
    for i in range(seconds):
        sleep(1)
        self.update_state(
            state='PROGRESS',
            meta={'current': i + 1, 'total': seconds},
        )
        logger.info(f'Dummy progress: {i+1} / {seconds} sec')
