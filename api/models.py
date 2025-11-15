from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    nome = models.CharField(max_length=120)
    sigla = models.CharField(max_length=20, blank=True)
    localidade = models.CharField(max_length=120, blank=True)
    pais = models.CharField(max_length=80, default="Portugal")

    def __str__(self):
        return self.nome


class Athlete(models.Model):
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    região = models.CharField(max_length=120, blank=True)
    clube = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    aprovado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Season(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    is_manual = models.BooleanField(default=False)
    bonus_type = models.CharField(max_length=50, default="default")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Race(models.Model):
    nome = models.CharField(max_length=120)
    data = models.DateField()
    localidade = models.CharField(max_length=120)
    distancia_km = models.FloatField()
    tipo = models.CharField(max_length=50)
    dificuldade_factor = models.FloatField(default=1.0)
    tempo_vencedor_segundos = models.IntegerField()

    temporada_automatica = models.ForeignKey(
        Season,
        on_delete=models.SET_NULL,
        null=True,
        related_name='races_automaticas',
    )

    temporadas_manuais = models.ManyToManyField(
        Season,
        blank=True,
        related_name='races_manuais',
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Result(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    tempo_segundos = models.IntegerField()
    posicao_geral = models.IntegerField(null=True, blank=True)
    posicao_escalao = models.IntegerField(null=True, blank=True)
    fonte = models.CharField(max_length=120, blank=True)
    is_official = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    data_submissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.athlete} - {self.race}"
