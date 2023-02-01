def solution(n):
    answer = -1
    x = n ** 0.5
    if x == int(x):
        answer = ( x + 1 ) ** 2
    return answer