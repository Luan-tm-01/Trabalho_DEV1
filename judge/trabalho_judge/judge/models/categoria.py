from .base_model import *
from django.core.validators import MinLengthValidator


class Categoria(BaseModel):
    nome = models.CharField(max_length=50,
                            help_text="Digite a Categoria",
                            validators=[MinLengthValidator(5)])
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[MinLengthValidator(5)])
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Categoria: {self.nome}'