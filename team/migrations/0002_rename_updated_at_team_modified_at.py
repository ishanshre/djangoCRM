# Generated by Django 4.1.7 on 2023-02-22 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='updated_at',
            new_name='modified_at',
        ),
    ]
