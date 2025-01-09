from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

class Tag(models.Model):
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    LABEL_CHOICES = [
        ('WEB', 'Web'),
        ('DS', 'Data Science'),
        ('FIN', 'Finanzas'),
    ]

    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)
    label = CharField(max_length=20, choices=LABEL_CHOICES, default='WEB')
    sublabels = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title
