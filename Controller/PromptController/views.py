from tokenize import String

from django.shortcuts import render
from django.http import JsonResponse

from Service.PromptService import obtenerRespuestaPrompt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def prompt(request):
    mensaje = request.GET.get("mensaje")
    if mensaje:
        respuesta = obtenerRespuestaPrompt(mensaje)
        return JsonResponse(respuesta, safe=False, status=200)
    else:
        return JsonResponse({"error": "Debe enviar un parámetro 'mensaje'"}, status=400)