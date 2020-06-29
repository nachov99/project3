# Generated by Django 3.0.7 on 2020-06-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200625_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DinnerPlatter', models.ManyToManyField(related_name='DinnerPlatter', to='orders.DinnerPlatter')),
                ('pasta', models.ManyToManyField(related_name='pasta', to='orders.pasta')),
                ('pizza', models.ManyToManyField(related_name='pizza', to='orders.pizza')),
                ('salad', models.ManyToManyField(related_name='salad', to='orders.salad')),
                ('sub', models.ManyToManyField(related_name='sub', to='orders.sub')),
                ('topping', models.ManyToManyField(related_name='topping', to='orders.topping')),
            ],
        ),
    ]