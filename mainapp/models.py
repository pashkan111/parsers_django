from django.db import models


class Article(models.Model):
    CHOISES = (
    ('POSITIVE', 'Положительная'),
    ('NEGATIVE', 'Отрицательная'),
)

    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Текст статьи')
    href = models.CharField(max_length=200, verbose_name='Ссылка на статью')
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
    parsed_at = models.DateTimeField(auto_now_add=True, verbose_name='Время парсинга')
    wrote_at = models.DateTimeField(verbose_name='Время выхода статьи', null=True)
    title_score_2 = models.FloatField(verbose_name='Оценка алгоритма скоринга', null=True)
    title_score_3 = models.FloatField(verbose_name='Оценка алгоритма скоринга', null=True)
    title_score_4 = models.FloatField( verbose_name='Оценка алгоритма скоринга', null=True)
    text_score_2 = models.FloatField( verbose_name='Оценка алгоритма скоринга', null=True)
    text_score_3 = models.FloatField(verbose_name='Оценка алгоритма скоринга', null=True)
    text_score_4 = models.FloatField(verbose_name='Оценка алгоритма скоринга', null=True)
    human_classification = models.CharField(
        choices=CHOISES,
        default='POSITIVE',
        verbose_name='Оценка',
        max_length=100,
        null=True
        )

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

    def __str__(self) -> str:
        return self.title


class Sign(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название акции (BTC, ETH, AAPL)')
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name='Акция'
        verbose_name_plural='Акции'

    def __str__(self) -> str:
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название источника информации (Coinbase, bloomberg, etc)')
    href = models.CharField(max_length=200, verbose_name='Ссылка на главную')
    description = models.TextField(verbose_name='Описание источника информации')
    theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name='Источник'
        verbose_name_plural='Источники'

    def __str__(self) -> str:
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название темы')
    class Meta:
        verbose_name='Тема'
        verbose_name_plural='Темы'

    def __str__(self) -> str:
        return self.name
