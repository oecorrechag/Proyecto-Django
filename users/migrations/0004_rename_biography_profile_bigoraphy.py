# Generated by Django 3.2.8 on 2021-11-05 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_bigoraphy_profile_biography'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='biography',
            new_name='bigoraphy',
        ),
    ]
