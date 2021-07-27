from django.core.management.base import BaseCommand
from parcers.main import main
from mainapp.models import Article, Theme, Source


class Command(BaseCommand):
    help = 'Запускает парсер'

    def handle(self, *args, **kwargs):
        theme = Theme.objects.first()
        articles = main()
        for article in articles:
            source, created = Source.objects.get_or_create(
                name=article['source_name'],
                href=article['source_href'],
                description='description...',
                theme=theme
                )
            title = article['title']
            href = article['href']
            text = article['text']
            new_article = Article(
                title=title,
                href=href,
                text=text
            )
            new_article.source = source
            if not Article.objects.filter(title=title):
                new_article.save()
        return 'Статьи были добавлены в базу данных'