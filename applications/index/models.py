from django.db import models
from django.db.models.fields import CharField, URLField


class UserProfile(models.Model):
    nombre_completo = CharField(max_length=100)
    titulo_profesional = CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to="index/images")
    github_url = URLField(blank=True)
    linkedin_url = URLField(blank=True)
    discord_url = URLField(blank=True)
    cv_file = models.FileField(upload_to='index/pdf', blank=True)
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        return self.nombre_completo
