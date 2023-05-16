from django.db import models

class Letras(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    letra = models.TextField(max_length=1220, blank=False, null=False)

    class Meta:
        verbose_name = 'Letras'
        verbose_name_plural = 'Letras'
        ordering = ['id']

    def __str__(self):
        return self.nombre
