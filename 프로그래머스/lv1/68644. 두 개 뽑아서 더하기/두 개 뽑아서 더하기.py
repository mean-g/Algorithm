# import itertools

# def solution(numbers):
#     answer = []
#     for i in itertools.combinations(numbers, 2):
#         answer.append (sum(i))
#     return sorted(set(answer))

from itertools import combinations

def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))