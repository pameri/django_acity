from celery import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task()
def add(x, y):
    logger.info('Se ha agregado %s + %s' % (x, y))
    return x + y