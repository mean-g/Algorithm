def solution(a, b):
    # answer = 0
    # for i in range(len(a)):
    #     answer += a[i] * b[i]
    # return answer
    return sum([a[i] * b[i] for i in range(len(a))])