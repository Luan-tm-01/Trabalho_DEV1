from django.core.exceptions import ValidationError
from datetime import date

class ValidarIdadeMinima:
    def __call__(self, value):
        hoje = date.today()
        idade = hoje.year - value.year - (
            (hoje.month, hoje.day) < (value.month, value.day)
        )

        if idade < 10:
            raise ValidationError("A pessoa deve ter no mínimo 10 anos.")