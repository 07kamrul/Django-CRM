# Generated by Django 2.1.7 on 2020-04-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200425_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]