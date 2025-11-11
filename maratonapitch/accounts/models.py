from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TIPO_PUBLICO_CHOICES = (
        ('INTERNO', 'Público Interno'),
        ('EXTERNO', 'Público Externo'),
    )
    tipo_publico = models.CharField(
        max_length=10,
        choices=TIPO_PUBLICO_CHOICES,
        default='EXTERNO',
    )

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_tipo_publico_display()})"
