# Generated by Django 4.1.7 on 2023-05-03 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_rename_user_pictures_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='opinion',
            new_name='feedback',
        ),
        migrations.RenameField(
            model_name='pictures',
            old_name='user_name',
            new_name='username',
        ),
    ]
