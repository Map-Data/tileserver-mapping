# Generated by Django 3.0.6 on 2020-05-28 18:34

from django.db import migrations, models
import tileservermapping.osm_data.models
import tileservermapping.osm_data.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SqlDump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(help_text='Slippy map coordinate X')),
                ('y', models.IntegerField(help_text='Slippy map coordinate Z')),
                ('z', models.IntegerField(help_text='Slippy map coordinate Z')),
                ('file', models.FileField(default=None, null=True, storage=tileservermapping.osm_data.storage.OverwriteStorage(), upload_to=tileservermapping.osm_data.models.gen_sql_dump_location)),
            ],
            options={
                'unique_together': {('x', 'y', 'z')},
            },
        ),
        migrations.CreateModel(
            name='PlanetDump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(help_text='Slippy map coordinate X')),
                ('y', models.IntegerField(help_text='Slippy map coordinate Y')),
                ('z', models.IntegerField(help_text='Slippy map coordinate Z (zoom)')),
                ('file', models.FileField(default=None, null=True, storage=tileservermapping.osm_data.storage.OverwriteStorage(), upload_to=tileservermapping.osm_data.models.gen_planet_dump_location)),
            ],
            options={
                'unique_together': {('x', 'y', 'z')},
            },
        ),
    ]
