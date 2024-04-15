# Generated by Django 5.0.4 on 2024-04-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]