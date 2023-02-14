from django.db import models

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Header")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Text")
    author = models.CharField(max_length=500, null=False, blank=False, verbose_name="Author")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date and time of refresh")

    asd = models.DateTimeField(auto_now=True, verbose_name="Date and time of refresh")


    def __str__(self):
        return f"{self.author} - {self.title}"
# Create your models here.
