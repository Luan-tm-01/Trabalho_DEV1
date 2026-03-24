from .base_model import *
from django.core.validators import MinLengthValidator
from judge.enumerations import Dificuldade, Idioma, LimiteMemoria, LimiteTempo, Nota

class Problema(BaseModel):
    cod = models.CharField(max_length=20, unique=True,
                           verbose_name="Código",
                           validators=[MinLengthValidator(4)])
    titulo = models.CharField(max_length=200,
                              verbose_name="Título",
                              validators=[MinLengthValidator(5)])
    enunciado = models.TextField(max_length=5000,
                                 verbose_name="Enunciado",
                                 validators=[MinLengthValidator(10)])
    enunciado_entrada = models.TextField(max_length=2000,
                                 verbose_name="Entrada",
                                 validators=[MinLengthValidator(10)])
    enunciado_saida = models.TextField(max_length=2000,
                                 verbose_name="Saída",
                                 validators=[MinLengthValidator(10)])
    dificuldade = models.IntegerField(choices=Dificuldade)
    idioma = models.CharField(max_length=20,
                              help_text="Selecione seu Idioma",
                              choices=Idioma)
    fonte = models.CharField(max_length=150,
                             validators=[MinLengthValidator(3)])
    limite_tempo_ms = models.IntegerField(default=LimiteTempo.S1,
                                       choices=LimiteTempo)
    limite_memoria_mb = models.CharField(default=LimiteMemoria.MB32,
                                       choices=LimiteMemoria)
    publico = models.BooleanField(default=True)
    nota = models.IntegerField(default=Nota.NOTA1,
                            choices=Nota)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.titulo}'
