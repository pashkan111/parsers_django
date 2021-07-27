from celery import shared_task
from parcers.main import main
from .models import Article, Theme, Source

@shared_task
def run_parsers():
    articles = main()
    for article in articles:
        source, created = Source.objects.get_or_create(
            name=article['source_name'],
            href=article['source_href'],
            description='description...',
            )
        
        title = article['title']
        if not Article.objects.filter(title=title):
            href = article['href']
            text = article['text']
            new_article = Article(
                title=title,
                href=href,
                text=text
            )
            new_article.source = source
        
            new_article.save()

    return 'Статьи были добавлены в базу данных'
