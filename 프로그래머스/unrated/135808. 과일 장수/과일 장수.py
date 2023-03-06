def solution(k, m, score):
    # answer = sorted(score, reverse=True)[m-1::m]
    # return sum(answer) * m
    return sum(sorted(score, reverse=True)[m-1::m]) * m