# Generated by Django 3.1.3 on 2021-02-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0013_auto_20210225_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='submited_File',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
