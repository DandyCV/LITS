from django.contrib import admin
from .models import Author, Editor, Article

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

class EditorAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Article, ArticleAdmin)