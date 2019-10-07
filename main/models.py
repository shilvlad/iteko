from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MainNews(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title
