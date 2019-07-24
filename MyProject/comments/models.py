from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    text = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.name + '\n\n' + self.text[:30]