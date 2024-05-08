def common_divisors(numbers):
    def get_divisors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    common = set(get_divisors(numbers[0]))
    for num in numbers[1:]:
        common &= set(get_divisors(num))
    return sorted(list(common))

numbers = [42, 12, 18]

print(common_divisors(numbers)) 