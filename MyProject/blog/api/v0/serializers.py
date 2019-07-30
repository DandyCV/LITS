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


class Comments(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False,  read_only=True)
    article = serializers.PrimaryKeyRelatedField(many=False, read_only=True)  # id user who wrote a comment
    text = serializers.CharField(max_length=2500)
    create = serializers.DateTimeField()
    update = serializers.DateTimeField()