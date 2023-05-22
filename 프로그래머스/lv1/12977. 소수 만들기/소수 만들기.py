import itertools

def solution(nums):
    answer = 0
    n_comb = list(itertools.combinations(nums, 3))
    
    for i in n_comb:
        i = sum(i)
        for j in range(2, i):
            if i % j == 0:
                break 
        else:
                answer += 1
                
    return answer

# import itertools

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     n_comb = list(itertools.combinations(nums, 3))

#     for j in n_comb:
#         if is_prime(sum(j)):
#             answer += 1

#     return answer