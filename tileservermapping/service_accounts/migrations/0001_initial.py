# Generated by Django 3.0.5 on 2020-05-07 16:21

from django.db import migrations, models
import tileservermapping.service_accounts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=120)),
                ('expiry', models.DateTimeField(default=tileservermapping.service_accounts.models.expiry_default)),
                ('token', models.CharField(default=tileservermapping.service_accounts.models.token_default, editable=False, max_length=32)),
            ],
        ),
    ]
