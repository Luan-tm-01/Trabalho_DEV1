from django.db import models
from .teste import Teste
from django.core.validators import MinValueValidator, MaxValueValidator

class Caso(Teste):
    peso = models.IntegerField(default=20,
                                validators=[MinValueValidator(1), MaxValueValidator(20)])
    
    def __str__(self):
        return f'Caso: {self.nome} | Problema: {self.problema}'