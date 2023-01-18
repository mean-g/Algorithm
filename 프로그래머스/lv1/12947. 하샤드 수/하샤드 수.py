def solution(x):
    answer = ()
    new_x  = list(map(int, str(x)))
    i      = x / sum(new_x)
    if int(i) == i:
        answer = 1
    else:
        answer = 0
    return bool(answer)