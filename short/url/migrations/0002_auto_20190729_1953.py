# Generated by Django 2.2.3 on 2019-07-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]