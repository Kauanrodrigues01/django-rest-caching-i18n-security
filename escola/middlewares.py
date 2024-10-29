# middlewares.py
from django.http import JsonResponse

class CustomRatelimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Verifica se a resposta é 403 e modifica a mensagem
        if response.status_code == 403:
            return JsonResponse(
                {'detail': 'Você foi bloqueado devido ao limite de requisições.'},
                status=429  # Você pode mudar para 429 se preferir
            )

        return response
