
def reverseSort(L):
    count = 0
    for i in range(len(L)-1):
        j = L.index(min(L[i:len(L)]))
        count += j-i+1
        L[i:j+1] = L[i:j+1][::-1]
    return count

for testcases in range(int(input())):
    a = int(input())
    L = list(map(int, input().split(maxsplit=a)))
    value = reverseSort(L)
    print('Case #{}: {}'.format(testcases+1, value))

