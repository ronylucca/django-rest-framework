from rest_framework import routers, serializers, viewsets
from .models import Programa, Radio, HorarioFuncionamento


class HorarioFuncionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioFuncionamento
        fields = ('dia_da_semana', 'inicio', 'fim')


class ProgramaSerializer(serializers.ModelSerializer):
    programacoes = HorarioFuncionamentoSerializer(many=True)

    class Meta:
        model = Programa
        fields = ('id', 'prioridade', 'nome', 'participacao', 'resumo', 'descricao', 'url_thumb', 'programacoes')


class RadioSerializer(serializers.ModelSerializer):
    programas = ProgramaSerializer(many=True)

    class Meta:
        model = Radio
        fields = ('id', 'nome', 'praca', 'estacao', 'url_streaming', 'programas')