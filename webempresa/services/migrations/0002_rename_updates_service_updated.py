# Generated by Django 5.0.7 on 2024-07-24 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='updates',
            new_name='updated',
        ),
    ]