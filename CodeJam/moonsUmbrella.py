def replacement(s, pos):
    if s[pos+1] != '?':
        s = s.replace(s[pos], s[pos+1], 1)
        return s
    else:
        return replacement(s, pos+1)


for test_cases in range(int(input())):
    L = list(map(str, input().split()))
    X = int(L[0])
    Y = int(L[1])
    s = L[2]
    pos = 0
    while pos < len(s):
        if s[pos] == '?':
            if pos == 0:
                s = replacement(s, pos)
            else:
                s = s.replace(s[pos], s[pos-1], 1) 
        pos += 1
    X = X * s.count('CJ')
    Y = Y * s.count('JC')
    print('Case #{}: {}'.format(test_cases+1, X+Y))
