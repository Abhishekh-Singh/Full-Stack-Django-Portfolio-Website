# Generated by Django 4.0.1 on 2022-01-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_project_sub_headline_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sub_headline',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
