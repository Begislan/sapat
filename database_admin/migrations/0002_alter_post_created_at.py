# Generated by Django 5.1.2 on 2024-10-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
