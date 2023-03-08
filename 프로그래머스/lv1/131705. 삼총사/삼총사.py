# def solution(number):
#     answer = 0
#     for i in range(len(number)-2):
#         for j in range(i + 1, len(number)-1):
#             for k in range(j + 1, len(number)):
#                 if number[i] + number[j] + number[k] == 0:
#                     answer += 1
#     return answer

import itertools

def solution(number):
    num_com = itertools.combinations(number, 3)
    return sum([1 if sum(num) == 0 else 0 for num in num_com])