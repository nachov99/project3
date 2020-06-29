# Generated by Django 3.0.7 on 2020-06-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200627_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='orders.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('Small', 'Small'), ('Large', 'Large')], max_length=64, null=True),
        ),
    ]
