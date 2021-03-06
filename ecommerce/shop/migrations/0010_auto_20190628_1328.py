# Generated by Django 2.2 on 2019-06-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190628_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='Choices',
            field=models.CharField(choices=[('s', 'sets'), ('hs', 'half sets'), ('n', 'nechlace'), ('r', 'rings'), ('e', 'earrigs'), ('b', 'bracelets')], default='s', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='caliber',
            field=models.FloatField(default=True),
        ),
    ]
