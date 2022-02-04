import numpy as np
import math

def smallestMultiple (x, y):

    range = np.arange(x, y+1)
    return np.lcm.reduce(range)

def sum_square_diff (num):
    sum_squares, sum_sqd = 0, 0
    for x in range(num + 1):

        sum_squares += (x * x)
        sum_sqd += x
        if x == num: sum_sqd = sum_sqd * sum_sqd

    # print(f"Quick math: {sum_sqd} - {sum_squares}")
    return sum_sqd - sum_squares


def prime_num (prime):
    #TODO: Super slow, speed this up?
    prime_list = []
    count = 2
    while len(prime_list) < prime:
        is_prime = True

        for x in range(2, count):
            if count % x == 0 and x != 0:
                is_prime = False
                break

        if is_prime == True: prime_list.append(count)
        count += 1

    return prime_list[-1]

def lrg_product_series ():
    series = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    adjacent_nums = temp_list = list(series[0:13])
    print(adjacent_nums)
    highest_num = 0
    # for x in series[13:]:
    #     temp_list.pop(0)
    #     temp_list.append(x)
    #     temp_num = math.prod(temp_list)
    #     if  temp_num > highest_num:
    #         highest_num = temp_num
    #         adjacent_nums = temp_list
                

    return f"Adjacent numbers: {adjacent_nums} Product: {highest_num} "