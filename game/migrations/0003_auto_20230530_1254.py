# Generated by Django 3.2.18 on 2023-05-30 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20230529_1114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]