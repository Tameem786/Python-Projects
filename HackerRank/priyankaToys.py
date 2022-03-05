import timeit

def toys(w):
    count = 0
    while len(w)>0:
        w.sort()
        count += 1
        # print([i for i in w  if i <= w[0] + 4])
        w = [x for x in w if x not in [i for i in w  if i <= w[0] + 4]]
    return count

if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(str(timeit.timeit('toys(w)', setup='from __main__ import toys, w')))
    print(result)