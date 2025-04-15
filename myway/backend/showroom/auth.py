from rest_framework.authentication import SessionAuthentication

class CustomSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Временно отключаем CSRF проверку для отладки