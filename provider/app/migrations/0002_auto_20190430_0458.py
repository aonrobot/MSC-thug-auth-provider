# Generated by Django 2.2 on 2019-04-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='redirect_uri',
            field=models.CharField(default='some thing', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='app_name',
            field=models.CharField(max_length=100),
        ),
    ]
