# Generated by Django 4.0.1 on 2022-09-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field', '0002_fieldapplication_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldapplication',
            name='level',
            field=models.CharField(choices=[('diploma', 'DIPLOMA'), ('bachelor', 'BACHELOR')], default='diploma', max_length=50),
        ),
    ]