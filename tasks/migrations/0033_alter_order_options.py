# Generated by Django 4.1.2 on 2022-11-26 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0032_recievmessages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'طلب', 'verbose_name_plural': ' الطلبات'},
        ),
    ]
