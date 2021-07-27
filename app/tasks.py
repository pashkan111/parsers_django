from celery import shared_task

@shared_task
def run_parsers():
    return 'Статьи были добавлены в базу данных'
