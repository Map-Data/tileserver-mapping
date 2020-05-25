# Generated by Django 3.0.5 on 2020-05-25 15:37

from django.db import migrations, models
import tileservermapping.osm_data.models
import tileservermapping.osm_data.storage


class Migration(migrations.Migration):

    replaces = [('osm_data', '0002_auto_20200525_1451'), ('osm_data', '0003_auto_20200525_1530')]

    dependencies = [
        ('osm_data', '0001_initial_squashed_0004_auto_20200524_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planetdump',
            name='file',
            field=models.FileField(default=None, null=True, upload_to=tileservermapping.osm_data.models.generate_file_name),
        ),
        migrations.AlterField(
            model_name='planetdump',
            name='file',
            field=models.FileField(default=None, null=True, storage=tileservermapping.osm_data.storage.OverwriteStorage(), upload_to=tileservermapping.osm_data.models.generate_file_name),
        ),
    ]
