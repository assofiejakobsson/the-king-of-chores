# Generated by Django 3.2.18 on 2023-05-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_delete_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]