# Generated by Django 3.2.8 on 2021-10-24 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='post',
            new_name='image',
        ),
    ]
