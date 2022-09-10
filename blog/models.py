from django.db import models

from utils.base_model import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to='articles')
    likes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.title}'
