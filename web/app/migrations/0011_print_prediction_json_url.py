# Generated by Django 2.1.7 on 2019-03-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190303_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='prediction_json_url',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
