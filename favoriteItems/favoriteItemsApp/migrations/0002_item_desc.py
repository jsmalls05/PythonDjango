# Generated by Django 2.2.4 on 2020-09-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favoriteItemsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
