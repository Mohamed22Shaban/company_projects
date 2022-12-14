# Generated by Django 4.1.2 on 2022-11-23 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_remove_clients_amount_remove_sales_cost_sales_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('items', models.JSONField(default=dict)),
                ('customer', models.JSONField(default=dict)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Completed')], default=0)),
                ('payment_method', models.IntegerField(choices=[(1, 'Stripe'), (2, 'Paypal')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='sales',
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.transaction')),
            ],
            options={
                'verbose_name': 'الترتيب',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
