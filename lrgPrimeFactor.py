def primeFactors(num):
    factors = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num /= div
        div = div + 1

    return max(factors)