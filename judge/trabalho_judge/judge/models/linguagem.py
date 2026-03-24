from .base_model import *
from django.core.validators import MinLengthValidator, MinValueValidator

class Linguagem(BaseModel):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Nome da Linguagem",
                            validators=[MinLengthValidator(3)])
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[MinLengthValidator(3)])
    compilador = models.CharField(max_length=80,
                                  validators=[MinLengthValidator(5)])
    versao =  models.CharField(max_length=50,
                               validators=[MinLengthValidator(3)])
    multiplicador_tempo = models.FloatField(validators=[MinValueValidator(1.0)])
    multiplicador_memoria = models.FloatField(validators=[MinValueValidator(1.0)])
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Linguagens"
