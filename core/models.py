from django.db import models

DIASDASEMANA = [
    (1, ("Segunda")),
    (2, ("Terça")),
    (3, ("Quarta")),
    (4, ("Quinta")),
    (5, ("Sexta")),
    (6, ("Sábado")),
    (7, ("Domingo")),
]


class HorarioFuncionamento(models.Model):

    dia_da_semana = models.IntegerField(
        choices=DIASDASEMANA,
        unique=False)
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return "%s %s %s" % (self.dia_da_semana, self.inicio, self.fim)

        class Meta:
            ordering = ('dia_da_semana',)


class Programa(models.Model):
    nome = models.CharField(max_length=50)
    participacao = models.CharField(max_length=100)
    resumo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    url_thumb = models.CharField(max_length=255)
    programacoes = models.ManyToManyField(HorarioFuncionamento)
    prioridade = models.IntegerField(unique=False)

    def __str__(self):
        return self.nome

        class Meta:
            ordering = ('prioridade',)


class Radio(models.Model):
    nome = models.CharField(max_length=40)
    praca = models.CharField(max_length=50)
    estacao = models.DecimalField(max_digits=3, decimal_places=1)
    programas = models.ManyToManyField(Programa)
    url_streaming = models.CharField(max_length=255)

    def __str__(self):
        return self.nome