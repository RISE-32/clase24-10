from django.http import JsonResponse
from saludo.application.services.saludar_service import SaludarService


def saludar_view(request):
    nombre = request.GET.get('nombre', 'Mundo')
    saludar_service = SaludarService()
    mensaje = saludar_service.ejecutar(nombre)

    return JsonResponse({'mensaje': mensaje})

