def solution(x):
    answer = ()
    new_x  = list(map(int, str(x)))
    i      = x / sum(new_x)
    if int(i) == i:
        answer = True
    else:
        answer = False
    return answer