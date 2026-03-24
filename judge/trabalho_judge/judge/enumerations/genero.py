from django.db import models

class Genero(models.TextChoices):
    MAN = "Homem", "Homem"
    WOMAN = "Mulher", "Mulher"
    NON_BINARY = "Não binário", "Não binário"
    NOT_INFORMED = "Não informado", "Não informado"
    ___ = "---", "---"
