from django.db import models
from .teste import Teste
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

class Exemplo(Teste):
    ordem = models.IntegerField(unique=True, default=1,
                                validators=[MinValueValidator(1), MaxValueValidator(10)])

    def clean(self):
        consulta = Exemplo.objects.filter(ordem=self.ordem,problema=self.problema).exclude(id=self.id).exists()

        if consulta:
            raise ValidationError({
                'ordem': "Erro ordem",
                'problema': "Erro problema"
            })

    def __str__(self):
        return f'Exemplo {self.ordem}'