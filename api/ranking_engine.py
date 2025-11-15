from .models import Athlete, Result

def calcular_pontuacao(result):
    r = result.race
    if result.tempo_segundos == 0:
        return 0
    ratio = r.tempo_vencedor_segundos / result.tempo_segundos
    return round(1000 * ratio * r.dificuldade_factor, 2)

def bonus_consistencia(results):
    return (len(results) // 3) * 5

def ranking_geral():
    tabela = []
    for atleta in Athlete.objects.filter(aprovado=True, ativo=True):
        results = Result.objects.filter(athlete=atleta, is_approved=True)
        pontos = sum(calcular_pontuacao(r) for r in results)
        pontos += bonus_consistencia(results)
        tabela.append({"atleta": atleta.nome, "pontos": pontos})
    return sorted(tabela, key=lambda x: x["pontos"], reverse=True)
