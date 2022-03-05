
if __name__ == '__main__':
    for C in range(int(input())):
        rawstr = ''.join([int(x)*'('+x+')'*int(x) for x in str(input())])
        for _ in range(9):
            rawstr = rawstr.replace(')(','')
        print('Case #{}: {}'.format(C+1, rawstr))
