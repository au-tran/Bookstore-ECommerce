# Generated by Django 2.2.6 on 2019-11-30 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191129_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='Image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=''),
        ),
    ]
