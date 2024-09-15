#lambda funcion
def filterUsersByScore(users, minScore):
    filteredUsersIterator = filter(lambda user: user['score'] >= minScore, users)
    
    filteredUsers = list(filteredUsersIterator)

    return filteredUsers

#list comprehension
def usersWithExtraPoints(users, extraScores):
    usersName = [user['name'] for user in users]
    scoresWithExtra = [min(user['score'] + extraScores,100) for user in users]
    workGroups = [user['workGroup'] for user in users]

    props = zip(usersName, scoresWithExtra, workGroups)
    usersWithExtra = [{"name": name, "score": score, "workGroup": workGroup} for name, score, workGroup in props]

    return usersWithExtra

#closure
def totalTeamScore(users):
    def totalTeam(workGroup):
        groupMembers = [user for user in users if user['workGroup'] == workGroup]
        return sum(member['score'] for member in groupMembers)

    return totalTeam

#higher-order function (função de alta ordem)
def applyReduction(function, users, deduction, workGroup):
    return [function(user, deduction, workGroup) for user in users]

def reduction(user, deduction, workGroup):
    if user["workGroup"] == workGroup:
        return {**user, "score": user["score"] - deduction}

    #Duplo asterisco garante a imutabilidade do dicionário original
    return {**user}
