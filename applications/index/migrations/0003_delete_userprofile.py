# Generated by Django 5.1.4 on 2025-01-08 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_alter_userprofile_cv_file_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
