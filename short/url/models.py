from django.db import models


# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=2000, unique=True)

    short_url = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.short_url = settings.BASE_URL + encode_url(self.id)
    #     self.save(*args, **kwargs)
