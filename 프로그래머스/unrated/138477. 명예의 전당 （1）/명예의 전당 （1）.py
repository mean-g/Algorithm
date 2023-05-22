def solution(k, score):
    answer = []
    honor  = []
    
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
            
        elif score[i] > min(honor):
            honor.append(score[i])
            honor.remove(min(honor))

        answer.append(min(honor))
            
    return answer