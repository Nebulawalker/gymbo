from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


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
        verbose_name='Количество показов',
        default=0,
        editable=False
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
        max_length=200,
        null=False,
        unique=True
    )
    content_blocks = models.ManyToManyField(
        to=ContentBlock,
        verbose_name='Контент-блоки',
        related_name='content_blocks'
    )
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'