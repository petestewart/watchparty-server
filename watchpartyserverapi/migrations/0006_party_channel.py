# Generated by Django 3.1.4 on 2021-01-02 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyserverapi', '0005_channelmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='channel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='watchpartyserverapi.channel'),
        ),
    ]