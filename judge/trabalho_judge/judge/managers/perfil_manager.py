from django.utils import timezone
from datetime import timedelta
from .base_manager import BaseManager

class PerfilManager(BaseManager):

    def premium_recentes_do_pais(self, pais, dias):
        limite = timezone.now() - timedelta(days=dias)

        return self.filter(
            premium=True,
            pais=pais,
            membro_desde__gte=limite
        )