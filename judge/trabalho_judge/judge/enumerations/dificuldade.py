from django.db import models

class Dificuldade(models.IntegerChoices):
    LV1 = 1, "Muito Fácil"
    LV2 = 2, "Fácil"
    LV3 = 3, "Básico"
    LV4 = 4, "Intermediário"
    LV5 = 5, "Intermediário Alto"
    LV6 = 6, "Difícil"
    LV7 = 7, "Muito Difícil"
    LV8 = 8, "Avançado"
    LV9 = 9, "Muito Avançado"
    LV10 = 10, "Perito"