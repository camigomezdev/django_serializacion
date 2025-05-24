
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


# class APIKeyAuthentication(BasicAuthentication):

#     def authenticate(self, request):
#         api_key = request.headers.get('X-CODIGO-FACILITO')

#         if not api_key:
#             raise AuthenticationFailed("Clave invalida o faltante!")

#         user = User.objects.get(id=api_key)

#         return (user, None)


class JWTWithAPIKey(JWTAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)

        if result is None:
            return None

        user, validate_toke = result

        api_key = request.headers.get('X-CODIGO-FACILITO')

        if not api_key or api_key != "supersegura123":
            raise AuthenticationFailed("Clave invalida o faltante!")

        return (user, validate_toke)
