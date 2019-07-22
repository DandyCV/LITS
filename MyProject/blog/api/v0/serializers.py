from rest_framework import serializers

from blog.models import (User, Author, Editor,  Article)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        mode = User
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    editor = UserSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'