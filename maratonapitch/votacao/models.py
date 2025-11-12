from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Startup(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    integrantes = models.CharField(max_length=255, blank=True)
    area_atuacao = models.CharField(max_length=150, blank=True)
    is_votacao_aberta = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    @property
    def total_votos(self):
        return self.votos.count()



class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='votos')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'startup')  # 1 voto por usuário por startup

    def __str__(self):
        return f"{self.usuario} → {self.startup}"


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario} em {self.startup}"
