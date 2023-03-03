def solution(d, budget):
    answer = 0
    min_d  = 0
    
    for i in sorted(d):
        if min_d + i <= budget:
            min_d  += i
            answer += 1
    return answer