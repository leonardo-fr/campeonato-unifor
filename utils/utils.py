#Função para ordenar usuários da pontuação maior para a menor usando Selection Sort
def sortedUsersByScore(users):
    #lista de index para iterar pela lista de usuários
    usersList = range(len(users))

    #percorre a lista de index criada na etapa anterior
    for i in usersList:
        #define o index do usuário com maior pontuação como index atual
        maxIndex = i

        #lista de index para iterar pela sublista atual de usuários
        usersSublist = range(i + 1, len(users))
        for j in usersSublist:
            highestScoringUserFound = users[j]['score'] > users[maxIndex]['score']

            if highestScoringUserFound:
                # Atualiza o maxIndex se foi encontrado um usuário com maior pontuação
                maxIndex = j

        #troca a posição do usuário atual com o usuário com maior pontuação encontrado
        temp = users[i]
        users[i] = users[maxIndex]
        users[maxIndex] = temp

    return users