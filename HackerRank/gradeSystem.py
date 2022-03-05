
def getTotalX(a, b):
    a_fact = []
    num = 1
    notFound = 0
    while True:
        if notFound > 100:
            break
        count = 0
        for i in a:
            if num%i == 0:
                count += 1
            else: 
                break
        if count == len(a):
            b_count = 0
            for i in b:
                if i%num == 0:
                    b_count += 1
                else:
                    break
            if b_count == len(b):
                a_fact.append(num)
                num += 1
                continue
            if b_count != len(b):
                notFound += 1
                num += 1
                continue
        if count != len(a):
            notFound += 1
            num += 1
            continue
    return a_fact

a = [1]
b = [100]
print(getTotalX(a, b))