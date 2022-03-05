test_cases = int(input())

case_result = []

if 1 <= test_cases and 100<=test_cases:

    for i in range(test_cases):
        count = 0
        num_of_houses, my_budget = input().split()
        my_budget = int(my_budget)
        list_of_house_price = list(map(int, input().split()))
        if 1 <= my_budget and pow(10,5)<=my_budget:
            list_of_house_price.sort()
            for item in list_of_house_price:
                if 1<=item and 1000<=item:
                    if my_budget >= item:
                        my_budget -= item
                        count += 1
                    else:
                        continue
            case_result.append(count)

    for i in range(test_cases):
        print('Case #{0}: {1}'.format(i+1, case_result[i]))

        