# Generated by Django 3.1.4 on 2021-01-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyserverapi', '0012_auto_20210104_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(default='avatar.jpeg', upload_to='images/avatars'),
        ),
    ]
