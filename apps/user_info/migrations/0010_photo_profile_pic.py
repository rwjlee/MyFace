# Generated by Django 2.0.4 on 2018-04-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0009_auto_20180427_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='profile_pic',
            field=models.IntegerField(null=True),
        ),
    ]
