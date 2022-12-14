# Generated by Django 4.1.2 on 2022-11-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_remove_order_updated_at_remove_sales_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecievMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('message', models.TextField(null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]
