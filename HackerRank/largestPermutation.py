def largestPermutation(k, arr):
    a = dict(enumerate(arr))
    b = {v:k for k,v in a.items()}
    l = len(arr)
    print('a = {0} \nb = {1} \nl = {2}'.format(a, b, l))
    for i in range(l):
        if k and a[i]!=l-i:
            x = a[i]
            y = b[l-i]
            a[i] = l-i
            a[y] = x
            b[x] = y
            print('i = {0} | x = {1} | y = {2} | a[i] = {3} | a[y] = {4} | b[x] = {5} | k = {6} | l-i = {7}'.format(i, x, y, a[i], a[y], b[x], k, l-i))
            k-=1
        yield a[i]
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(*largestPermutation(k, arr))