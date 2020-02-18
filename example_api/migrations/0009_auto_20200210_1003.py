# Generated by Django 3.0.2 on 2020-02-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_api', '0008_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-publish',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='static/userRoom/img'),
        ),
    ]
