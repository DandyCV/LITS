from rest_framework import serializers
from django.conf import settings
from short_url import encode_url

from.models import Url


class UrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(read_only=True)
    class Meta:
        model = Url
        fields = ('url', 'short_url', 'created')

    def create(self, validated_data):
        url = Url.objects.create(**validated_data)
        url.short_url = settings.BASE_URL + encode_url(url.id)
        url.save()

        return url
