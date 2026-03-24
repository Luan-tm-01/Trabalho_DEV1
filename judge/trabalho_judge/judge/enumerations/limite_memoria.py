from django.db import models

class LimiteMemoria(models.TextChoices):
    MB8 = "8 MB", "8 MB"
    MB16 = "16 MB", "16 MB"
    MB32 = "32 MB", "32 MB"
    MB64 = "64 MB", "64 MB"
    MB128 = "128 MB", "128 MB"
    MB256 = "256 MB", "256 MB"
