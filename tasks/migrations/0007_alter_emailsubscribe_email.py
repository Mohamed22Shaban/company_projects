# Generated by Django 4.1.2 on 2022-10-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_project_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscribe',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
