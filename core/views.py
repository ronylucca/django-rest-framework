from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse

from .models import Programa, Radio
from .serializers import ProgramaSerializer, RadioSerializer


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer

    def obtem_programacao_radio(request, radio):
        try:
            radio = Radio.objects.get(nome=radio)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)

        serializer_class = RadioSerializer(radio)
        return JsonResponse(['Ao vivo:', serializer_class.data], safe=False)