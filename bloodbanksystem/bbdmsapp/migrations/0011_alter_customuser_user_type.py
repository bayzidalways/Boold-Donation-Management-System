# Generated by Django 5.2.1 on 2025-06-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbdmsapp', '0010_donorreg_name_alter_donorreg_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'requester'), (1, 'admin'), (2, 'donor')], default=1, max_length=50),
        ),
    ]
