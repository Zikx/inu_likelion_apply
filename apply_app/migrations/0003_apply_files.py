# Generated by Django 3.0.3 on 2020-03-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_app', '0002_auto_20200310_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='files',
            field=models.FileField(null=True, upload_to='upload/files/'),
        ),
    ]
