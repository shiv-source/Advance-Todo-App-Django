# Generated by Django 3.0.8 on 2020-08-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='completed at'),
        ),
    ]
