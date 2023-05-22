import itertools

def solution(nums):
    answer = 0
    n_comb = list(itertools.combinations(nums, 3))
    
    for i in n_comb:
        s = sum(i)
        for j in range(2, s):
            if s % j == 0:
                break 
        else:
                answer += 1
                
    return answer