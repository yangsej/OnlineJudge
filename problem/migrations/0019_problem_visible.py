# Generated by Django 3.0.8 on 2020-10-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0018_problem_share_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
