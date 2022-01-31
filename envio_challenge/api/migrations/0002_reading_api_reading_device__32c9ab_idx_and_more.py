# Generated by Django 4.0.1 on 2022-01-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='reading',
            index=models.Index(fields=['device_id'], name='api_reading_device__32c9ab_idx'),
        ),
        migrations.AddIndex(
            model_name='reading',
            index=models.Index(fields=['customer_id'], name='api_reading_custome_f05f3f_idx'),
        ),
    ]
