# Generated by Django 2.2.4 on 2019-09-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='finished_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
