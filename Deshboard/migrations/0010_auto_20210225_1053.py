# Generated by Django 3.1.3 on 2021-02-25 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0009_auto_20210225_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createproject',
            name='Complete_Review',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='createproject',
            name='Complete_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createproject',
            name='assigned_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
