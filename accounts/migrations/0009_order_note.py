# Generated by Django 2.1.7 on 2020-05-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200425_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]