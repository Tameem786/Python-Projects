
for i in range(int(input())):
    times = []
    largest = 0
    smallest = 0
    s = ''
    for j in range(int(input())):
        start = list(map(int, input().split()))
        times.append([start[0], start[1]])
        if start[0] < smallest:
            smallest = start[0]
        if start[1] > largest:
            largest = start[1]
        if j > 0:
            #task 1 endTime > task 2 startTime
            if max(times[j-1][0], times[j][0]) < min(times[j-1][1], times[j][1]):
                if s[len(s)-1] is 'C':
                    s += 'J'
                    continue
                else:
                    s += 'C'
                    continue
            else:
                s += s[len(s)-1]
                continue
        s = 'C'   
    if [smallest, largest] in times:
        s = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(i+1, s))



