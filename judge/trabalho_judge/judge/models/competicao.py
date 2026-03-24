from .base_model import *
from django.core.validators import MinLengthValidator, MinValueValidator


class Competicao(BaseModel):
    nome = models.CharField(max_length=200,
                            validators=[MinLengthValidator(5)])
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[MinLengthValidator(3)])
    descricao = models.TextField(max_length=1000,
                                 validators=[MinLengthValidator(5)])
    url = models.URLField(null=True, blank=True,
                          verbose_name="URL")
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    freeze = models.DateTimeField()
    publico = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now_add=True)
    penalidade = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Competição: {self.nome} | Início: {self.inicio}'

    class Meta:
        verbose_name_plural = "Competições"
