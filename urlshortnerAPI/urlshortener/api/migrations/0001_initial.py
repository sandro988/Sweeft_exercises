# Generated by Django 4.0.6 on 2022-07-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=250)),
                ('short_url', models.URLField(max_length=10)),
                ('visit_count', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
