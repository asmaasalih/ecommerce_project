# Generated by Django 2.2.2 on 2019-06-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190621_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(default='post_img/default.png', upload_to='post_img/'),
        ),
    ]
