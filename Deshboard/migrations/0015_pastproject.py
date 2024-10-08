# Generated by Django 3.1.3 on 2021-02-28 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0014_formdata_submited_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='pastProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, unique=True)),
                ('project_description', models.TextField()),
                ('estimated_budget', models.CharField(max_length=30, null=True)),
                ('estimated_project_duration', models.CharField(max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
