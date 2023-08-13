from django.db import models


class ContentBlock(models.Model):
    title = models.CharField(
        verbose_name='Заголовок контент-блока',
        max_length=200
    )
    video_url = models.URLField(
        verbose_name='Ссылка на видео',
        max_length=200
    )
    views = models.IntegerField(
        verbose_name='Количество показов'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Контент-блок'
        verbose_name_plural = 'Контент-блоки'


class Page(models.Model):
    title = models.CharField(
        verbose_name='Заголовок страницы',
        max_length=200
    ) 
    slug = models.SlugField(
        verbose_name='Название в виде url',
        max_length=200
    )
    content_blocks = models.ManyToManyField(
        to=ContentBlock,
        verbose_name='Контент-блоки',
        related_name='content_blocks'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'