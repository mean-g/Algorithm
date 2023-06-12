def solution(n, lost, reserve):
    new_lo = set(lost) - set(reserve)
    new_re = set(reserve) - set(lost)
    
    for i in new_re:
        if i - 1 in new_lo:
            new_lo.remove(i - 1)
        elif i + 1 in new_lo:
            new_lo.remove(i + 1)
    return n - len(new_lo)