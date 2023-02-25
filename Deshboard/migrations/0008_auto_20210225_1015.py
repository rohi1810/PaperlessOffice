# Generated by Django 3.1.3 on 2021-02-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0007_auto_20210224_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='createproject',
            name='Complete_Review',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='createproject',
            name='Complete_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='govermentuserprofile',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='govermentuserprofile',
            name='experiance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='govermentuserprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizationuserprofile',
            name='experiance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizationuserprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizationuserprofile',
            name='total_project',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='Position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='experiance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddConstraint(
            model_name='createproject',
            constraint=models.CheckConstraint(check=models.Q(('Complete_Review__gte', 1), ('Complete_Review__lte', 10)), name='A Complete_Review value is valid between 1 and 10'),
        ),
    ]
