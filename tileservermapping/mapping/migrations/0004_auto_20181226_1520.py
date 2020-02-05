# Generated by Django 2.0.6 on 2018-12-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0003_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='host',
            field=models.CharField(default='127.0.0.1', max_length=80),
        ),
        migrations.AddField(
            model_name='server',
            name='scheme',
            field=models.CharField(default='http', max_length=10),
        ),
        migrations.AddField(
            model_name='server',
            name='url_postfix',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='server',
            name='url',
            field=models.CharField(default='512/all/{z}/{x}/{y}.{format}', max_length=80),
        ),
    ]
