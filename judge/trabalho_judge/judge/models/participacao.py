from django.db import models
from judge.models import BaseModel, Perfil, Competicao
from django.core.validators import MinValueValidator


class Participacao(BaseModel):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)
    registro = models.DateTimeField()
    oficial = models.BooleanField(default=True)
    total_pontos = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = "Participações"

    def __str__(self):
        return f'Participante: {self.perfil.user}'
