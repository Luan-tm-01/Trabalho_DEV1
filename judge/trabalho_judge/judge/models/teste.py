from .base_model import *
from django.core.validators import MinLengthValidator
from .problema import Problema

class Teste(BaseModel):
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80,
                            validators=[MinLengthValidator(5)])
    dados_entrada = models.TextField(max_length=80,
                            validators=[MinLengthValidator(1)],
                            verbose_name="Entrada")
    dados_saida = models.TextField(max_length=80,
                            validators=[MinLengthValidator(1)],
                            verbose_name="Saída")
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models. DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome}'