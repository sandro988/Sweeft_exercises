# Generated by Django 4.0.6 on 2022-07-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_link_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_url',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
