from django.db import models

class Idioma(models.TextChoices):
    PT_BR = "Português do Brasil", "Português do Brasil"
    EN_US = "Inglês dos EUA", "Inglês dos EUA"
    ES_ES = "Espanhol da Espanha", "Espanhol da Espanha"
