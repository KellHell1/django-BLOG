from django.db import models


class Article(models.Model):
    title = models.TextField('Название', max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE,)
    name = models.CharField(max_length=80, verbose_name='')
    body = models.TextField(verbose_name='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Комментарий от пользователя '{self.name}' на пост '{self.post}'"






