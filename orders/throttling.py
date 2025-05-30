

from rest_framework.throttling import BaseThrottle
from django.utils.timezone import now
from datetime import timedelta


VISITS = {}


class CustomIPThrottle(BaseThrottle):
    def allow_request(self, request, view):
        ip = self.get_ident(request)
        now_time = now()

        # Inicializar lista si no existe
        if ip not in VISITS:
            VISITS[ip] = []

        # Limpiar visitas antiguas (1 min atrás)
        window = now_time - timedelta(minutes=1)
        VISITS[ip] = [visit for visit in VISITS[ip] if visit > window]

        if len(VISITS[ip]) >= 5:
            return False  # Excedió el límite

        VISITS[ip].append(now_time)
        return True
    
    def wait(self):
        return 60
