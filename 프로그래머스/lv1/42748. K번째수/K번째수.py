def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        n = array[commands[i][0] - 1 : commands[i][1]]
        sort_n = sorted(n)
        answer.append(sort_n[commands[i][2]-1])
    return answer