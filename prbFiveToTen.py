import numpy as np

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
