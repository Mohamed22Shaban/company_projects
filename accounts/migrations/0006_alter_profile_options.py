# Generated by Django 4.1.2 on 2022-12-13 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'الملف الشخصى', 'verbose_name_plural': 'الملفات الشخصيه'},
        ),
    ]
