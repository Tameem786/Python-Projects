# [10 5 20 20 4 5 2 25 1]

def breakingRecords(scores):
    highestScore = scores[0]
    lowestScore = scores[0]
    best = 0
    worst = 0
    for i in scores:
        if i > highestScore:
            highestScore = i
            best += 1
        if i < lowestScore:
            lowestScore = i
            worst += 1
    return [best, worst]

if __name__ == '__main__':
    # n = int(input())
    # scores = list(map(int, input().rstrip().split()))
    result = breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
    print(result)