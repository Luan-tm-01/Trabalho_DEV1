from django.db import models
from judge.models import BaseModel, Perfil, Problema, Linguagem
from judge.enumerations import StatusSubmission, Nota
from django.core.validators import MinValueValidator, MinLengthValidator


class Submissao(BaseModel):
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    codigo_fonte = models.TextField(max_length=10000,
                                    verbose_name="Código Fonte",
                                    validators=[MinLengthValidator(1)])
    status = models.CharField(max_length=50,
                              help_text="Selecione o Status da Submissão",
                              choices=StatusSubmission)
    submetido = models.DateTimeField()
    avaliado_em = models.DateTimeField()
    tempo_execucao_ms = models.IntegerField(validators=[MinValueValidator(1)])
    memoria_utilizada_kb = models.IntegerField(
        validators=[MinValueValidator(32)])
    nota = models.IntegerField(help_text="Selecione a Nota",
                               choices=Nota)
    log_execucao = models.TextField(max_length=1000,
                                    validators=[MinLengthValidator(1)])

    class Meta:
        verbose_name_plural = "Submissões"

    def __str__(self):
        return f'Submissão do Problema {self.problema} feita pelo Usuário {self.usuario}'
