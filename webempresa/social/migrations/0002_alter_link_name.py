# Generated by Django 5.0.7 on 2024-07-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Red social'),
        ),
    ]
