# Generated by Django 3.2.3 on 2022-04-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrand',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='static/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='static/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='carreview',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='static/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='cartype',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='static/%Y/%m/%d'),
        ),
    ]
