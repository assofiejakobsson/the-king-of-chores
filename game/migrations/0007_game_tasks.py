# Generated by Django 3.2.18 on 2023-05-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_remove_game_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='tasks',
            field=models.ManyToManyField(to='game.Todo'),
        ),
    ]