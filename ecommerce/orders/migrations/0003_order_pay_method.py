# Generated by Django 2.2 on 2019-07-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190708_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_method',
            field=models.CharField(choices=[('PP', 'paypal'), ('CD', 'Cash On Delivery')], default='Cash On ..', max_length=100, null=True),
        ),
    ]