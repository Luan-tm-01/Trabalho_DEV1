from django.db import models

class Nota(models.IntegerChoices):
    NOTA1 = 100, "100"
    NOTA2 = 150, "150"
    NOTA3 = 200, "200"
    NOTA4 = 250, "250"
    NOTA5 = 300, "300"
    NOTA6 = 400, "400"
    NOTA7 = 500, "500"
    NOTA8 = 600, "600"
    NOTA9 = 800, "800"
    NOTA10 = 1000, "1000"