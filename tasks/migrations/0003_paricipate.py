# Generated by Django 4.1.2 on 2022-10-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_project_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paricipate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
