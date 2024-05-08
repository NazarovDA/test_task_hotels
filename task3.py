def get_primes_in_range(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

min_num = 11
max_num = 20
print(get_primes_in_range(min_num, max_num))