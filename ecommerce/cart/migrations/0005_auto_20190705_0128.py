# Generated by Django 2.2 on 2019-07-04 21:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0013_auto_20190702_0843'),
        ('cart', '0004_auto_20190705_0012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='ShopingCart',
        ),
    ]
