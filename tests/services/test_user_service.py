import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from utils.utils import sortedUsersByScore
from services.user_service import (
    filterUsersByScore,
    usersWithExtraPoints,
    totalTeamScore,
    applyReduction,
    reduction
)

def filterUsersByScoreTest():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]
    minScore = 75

    usuariosFiltrados = filterUsersByScore(users, minScore)
    assert len(usuariosFiltrados) == 2, f"Não há somente 2 usuários com média maior ou igual a {minScore}:\n{users}"
    print("filterUsersByScoreTest(): Itens filtrados com sucesso.")

def usersWithExtraPointsTest():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]
    extraPoints = 15

    usuariosFiltrados = usersWithExtraPoints(users, extraPoints)

    assert usuariosFiltrados[0]["score"] == 85, f"Não foi somado os pontos corretamentes aos scores dos usuários."
    print("usersWithExtraPointsTest(): Pontos extras somados corretamente.")

def totalTeamScoreTest():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]

    workGroup = totalTeamScore(users)

    assert workGroup(1) == 175, f"Erro ao calcular pontuação total da equipe 1"
    print("totalTeamScoreTest(): Pontuação da equipe somada corretamente.")

def applyReductionTest():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]
    deductionPoints = 10

    resultado = applyReduction(reduction, users, deductionPoints, 1)

    assert resultado[0]["score"] == 60, f"Erro ao aplicar penalidade ao grupo 1"
    print("applyReductionTest(): Penalidade aplicada corretamente.")

def sortedUsersByScoreTest():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]

    resultado = sortedUsersByScore(users)

    assert resultado[0]["name"] == "Patrícia", f"Erro ao ordenar usuários pela maior pontuação. resultado: \n{resultado}"
    print("sortedUsersByScoreTest(): Ordenação aplicada corretamente.")

if __name__ == "__main__":
    print("---INÍCIO DOS TESTES UNITÁRIOS---")
    filterUsersByScoreTest()
    usersWithExtraPointsTest()
    totalTeamScoreTest()
    applyReductionTest()
    sortedUsersByScoreTest()
    print("TESTES FINALIZADOS COM SUCESSO!")