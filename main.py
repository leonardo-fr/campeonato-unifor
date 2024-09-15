from utils.utils import sortedUsersByScore
from services.user_service import (
    filterUsersByScore,
    usersWithExtraPoints,
    totalTeamScore,
    applyReduction,
    reduction
)


def main():
    users = [
        {"name": "Alice", "score": 70, "workGroup": 1},
        {"name": "Edgar", "score": 75, "workGroup": 2},
        {"name": "Patrícia", "score": 90, "workGroup": 2},
        {"name": "Ricardo", "score": 50, "workGroup": 1},
        {"name": "Suzanna", "score": 55, "workGroup": 1},
        {"name": "Eduardo", "score": 35, "workGroup": 2}
    ]

    minScore = 85
    extraScore = 15
    deductionPoints = 10
    
    print('###################################################')
    print('SEÇÃO - INFORMAÇÕES')
    print('Por favor, informe a pontuação mínima para ser aprovado: (default = 85)')
    try:
        minScoreInput = int(input())
        if(minScoreInput > 0 and minScoreInput < 100):
            minScore = minScoreInput

    except ValueError:
        print('Entrada inválida. a pontuação default será utilzada.')

    usuariosComPontuacaoExtra = usersWithExtraPoints(users, extraScore)

    usuariosFiltrados = filterUsersByScore(usuariosComPontuacaoExtra, minScore)

    print('###################################################')
    print('SEÇÃO - RESULTADOS PARCIAIS')
    print('Usuarios com pontuação parcial: ')
    print(users)
    print('---------------------------------------------------')
    print('SEÇÃO - RESULTADOS COM PONTUAÇÃO EXTRA')
    print('Usuarios com pontuação Extra: ')
    print(usuariosComPontuacaoExtra)
    print('---------------------------------------------------')
    print('SEÇÃO - PONTUAÇÃO DOS GRUPOS')

    workGroup = totalTeamScore(usuariosComPontuacaoExtra)

    print(f'Total do grupo 1: {workGroup(1)}')
    print(f'Total do grupo 2: {workGroup(2)}')
    print('###################################################')
    print('SEÇÃO - PENALIDADES')

    usuariosComPenalidades = getUsersComPenalidades(usuariosComPontuacaoExtra, deductionPoints)

    print('###################################################')
    print('SEÇÃO - RESULTADOS FINAIS')

    usuariosComPenalidadesEOrdenados = sortedUsersByScore(usuariosComPenalidades)
    print("Pontuação final dos usuários ordenados pela maior pontuação:")
    print(usuariosComPenalidadesEOrdenados)

    usuariosFiltrados = filterUsersByScore(usuariosComPenalidades, minScore)
    usuariosFiltradosEOrdenados = sortedUsersByScore(usuariosFiltrados)
    print('---------------------------------------------------')
    print(f'Usuarios com nota superior a média de {minScore}: ')
    print(usuariosFiltradosEOrdenados)

    print('---------------------------------------------------')
    print("Pontuação final dos grupos:")

    workGroup = totalTeamScore(usuariosComPenalidades)

    print(f'Total do grupo 1: {workGroup(1)}')
    print(f'Total do grupo 2: {workGroup(2)}')

    if workGroup(1) > workGroup(2):
        print("Grupo 1 foi campeão!")
    elif workGroup(1) < workGroup(2):
        print("Grupo 2 foi campeão!")
    else:
        print("Houve um empate técnico!")

    print('---------------------------------------------------')
    print('Usuário campeão individual:')
    print(usuariosFiltradosEOrdenados[0])

    print('#################( PROGRAMA ENCERRADO! )#####################')

def getUsersComPenalidades(users, deductionPoints):
    print(f'Algum grupo foi penalizado em {deductionPoints} pontos por usuário? (Sim/Não)')
    try:
        grupoFoiPenalizado = input()
    except ValueError:
        print("Resposta inválida.")
        return users

    if(grupoFoiPenalizado.lower() == 'sim' or grupoFoiPenalizado.lower() == 's'):
        print('Por favor, qual grupo foi penalizado: (1 ou 2)')

        try:
            grupoPenalizado = int(input())
        except ValueError:
            print('Grupo não foi informado corretamente.')
            return users

        if(grupoPenalizado == 1):
            return applyReduction(reduction, users, deductionPoints, 1)
        elif(grupoPenalizado == 2):
            return applyReduction(reduction, users, deductionPoints, 2)
        else:
            print('Não foi informado um grupo válido.')
            return users
    
    return users

if __name__ == "__main__":
    main()
