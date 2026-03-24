from django.db import models

class LimiteTempo(models.IntegerChoices):
    S1 = 1000, "1 segundo"
    S2 = 2000, "2 segundos"
    S3 = 3000, "3 segundos"
    S4 = 4000, "4 segundos"
    S5 = 5000, "5 segundos"
    S6 = 6000, "6 segundos"
    S7 = 7000, "7 segundos"
    S8 = 8000, "8 segundos"
    S9 = 9000, "9 segundos"
    S10 = 10000, "10 segundos"