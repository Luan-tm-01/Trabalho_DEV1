from django.db import models
from .base_model import *
from judge.models import Competicao, Problema
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class ProblemaCompeticao(BaseModel):
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    label = models.CharField(max_length=5,
                             validators=[MinLengthValidator(1)])
    pontos = models.IntegerField(default=100,
                                 validators=[MinValueValidator(1), MaxValueValidator(100)])
    ordem = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = "Problemas das Competições"

    def __str__(self):
        return f'{self.competicao.nome} - {self.problema}'