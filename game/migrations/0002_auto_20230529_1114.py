# Generated by Django 3.2.18 on 2023-05-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.todo'),
        ),
        migrations.AddField(
            model_name='game',
            name='guests',
            field=models.ManyToManyField(to='game.Guest'),
        ),
    ]