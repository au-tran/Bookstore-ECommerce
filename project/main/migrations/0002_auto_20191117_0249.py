# Generated by Django 2.2.6 on 2019-11-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Description',
        ),
        migrations.AlterField(
            model_name='textbook',
            name='Cond',
            field=models.CharField(choices=[('MINT', 'BRAND NEW'), ('LIKE NEW', 'LIKE NEW'), ('DECENT', 'GOOD'), ('FAIR', 'FAIR'), ('POOR', 'POOR')], default='MINT', max_length=10),
        ),
    ]
