# Generated by Django 4.2.4 on 2024-02-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='quality_status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='QualityCheck',
        ),
    ]
