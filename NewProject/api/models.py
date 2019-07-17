from django.db import models

# Create your models here.
dict_ = {
    "Monday": "Kyiv",
    "Tuesday": "Lviv",
    "Wednesday": "Odessa",
    "Thursday": "Kharkiv",
    "Friday": "Chernivtsi"
}

class Article(models.Model):   #будуэ відображення запису в БД на обєкт пайтону
    author = models.ForeignKey('auth.models.User', related_name='author', on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=128)
    text = models.TextField(max_lengh=2000)

    # class Meta:
    #     table = 'article'   #назва таблиці
    #     order_by = ['publish']    #сортування по колонці


class Comment(models.Model):
    class Meta():
        db_table = 'comment'
        verbose_name = 'Comment'
        verbous_name_plural = 'Comments'

    user = models.ForeignKey('auth.models.User', related_name='author', on_delete=models.CASCADE)
    text = models.TextField('Comment Text')
    create = models.DateTimeField('add', auto_now_add=True)
    moder = models.BooleanField(default=False)