# Generated by Django 3.0.3 on 2020-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_app', '0003_apply_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='files',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
