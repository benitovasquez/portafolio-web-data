# Generated by Django 5.1.4 on 2025-01-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_completo", models.CharField(max_length=100)),
                ("titulo_profesional", models.CharField(max_length=100)),
                (
                    "foto_perfil",
                    models.ImageField(
                        default="default-user.jpg", upload_to="profile_pics/"
                    ),
                ),
                ("github_url", models.URLField(blank=True)),
                ("linkedin_url", models.URLField(blank=True)),
                ("discord_url", models.URLField(blank=True)),
                ("cv_file", models.FileField(blank=True, upload_to="cv_files/")),
            ],
            options={
                "verbose_name": "Perfil de Usuario",
                "verbose_name_plural": "Perfiles de Usuario",
            },
        ),
    ]