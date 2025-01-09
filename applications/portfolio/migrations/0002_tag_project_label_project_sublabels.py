# Generated by Django 5.1.4 on 2025-01-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="label",
            field=models.CharField(
                choices=[("WEB", "Web"), ("DS", "Data Science"), ("FIN", "Finanzas")],
                default="WEB",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="sublabels",
            field=models.ManyToManyField(blank=True, to="portfolio.tag"),
        ),
    ]
