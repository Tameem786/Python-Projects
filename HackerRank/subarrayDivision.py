

def SubArrayDivision(arr, n):
    temp = []
    for i in range(len(arr)):
        for j in range(n):
            sub = []
            sub.append(arr[i])
            for k in range(n):
                if k==j:
                    continue
                else:
                    sub.append(arr[k])   
            temp.append(sub)
    return temp


if __name__ == '__main__':
    print(SubArrayDivision([2,1,4,5], 2))
