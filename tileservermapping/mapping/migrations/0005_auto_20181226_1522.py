# Generated by Django 2.0.6 on 2018-12-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0004_auto_20181226_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='url_postfix',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
