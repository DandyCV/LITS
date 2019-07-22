from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    editor = models.ManyToManyField(Editor, related_name='articles')
    title = models.CharField(max_length=120)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + '\n\n' + self.text[:100]