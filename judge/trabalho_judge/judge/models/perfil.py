from .base_model import *
from judge.enumerations import Idioma, Genero
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MinLengthValidator
from datetime import date

class Perfil(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento",
                                       help_text="Selecione a data de nascimento")
    pais = models.CharField(max_length=100,
                            verbose_name="País",
                            validators=[MinLengthValidator(3)])
    genero = models.CharField(max_length=40,
                              help_text="Selecione seu genero",
                              default=Genero.___,
                              choices=Genero)
    pagina_pessoal = models.URLField(max_length=150, null=True,
                                     verbose_name="Página Pessoal",
                                     help_text="Digite a URL de sua página pessoal",
                                     validators=[MinLengthValidator(15)])
    biografia = models.TextField(null=True)
    idioma = models.CharField(max_length=20,
                              help_text="Selecione seu Idioma",
                              choices=Idioma)
    premium = models.BooleanField(default=False)
    membro_desde = models.DateField(default=date.today)
    instituicao = models.CharField(max_length=120,
                                   verbose_name="Instituição",
                                   validators=[MinLengthValidator(3)])
    posicao_ranking = models.IntegerField(default=1, 
                                         validators=[MinValueValidator(0)])
    resolvidos = models.IntegerField(default=0, 
                                     validators=[MinValueValidator(0)])
    submetidos = models.IntegerField(default=0, 
                                     validators=[MinValueValidator(0)])
    treinador = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name_plural = "Perfis"

    def clean(self):
        if self.genero == Genero.___:
            raise ValidationError({
                'genero': "Selecione um Gênero"
            })
        