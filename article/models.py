from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    
    CATEGORIES = (
                ('Pemrograman', "Pemrograman"),
                ('Perwibuan', "Perwibuan"),
                ('Kehidupan', "Kehidupan"),
                ('Game', "Game"),
                ('Teknologi', "Teknologi"),
            )

    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = RichTextUploadingField()
    category = models.CharField(max_length=30, choices=CATEGORIES, default='')
    cover = models.ImageField(upload_to='covers/', null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

