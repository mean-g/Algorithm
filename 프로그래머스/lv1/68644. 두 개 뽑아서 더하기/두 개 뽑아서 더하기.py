import itertools

def solution(numbers):
    answer = []
    for i in itertools.combinations(numbers, 2):
        if sum(i) not in answer:
            answer.append (sum(i))
    return sorted(answer)