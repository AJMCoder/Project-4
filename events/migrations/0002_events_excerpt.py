# Generated by Django 5.0.4 on 2024-04-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]