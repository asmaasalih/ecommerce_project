# Generated by Django 2.2 on 2019-07-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20190701_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='caliber',
            field=models.CharField(choices=[('18', '18'), ('21', '21')], default='21', max_length=2),
        ),
    ]