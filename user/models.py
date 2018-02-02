from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    class Meta:
        ordering = ['-pk']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=80, verbose_name='Заголовок')
    content = models.TextField('Текст статьи')
    tags = models.ManyToManyField('Tag', blank=True,
                                  related_name='articles',
                                  verbose_name='Теги')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='articles',
                             verbose_name='Пользователь')

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta():
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField('Текст комментария')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name='Статья')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пользователь')

    def __str__(self):
        return self.text[:10]
