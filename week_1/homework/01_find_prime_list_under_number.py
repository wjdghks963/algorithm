input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for num in range(2, number + 1):
        for i in prime_list:
            if num % i == 0 and i * i <= num:
                break
        else:
            prime_list.append(num)

    return prime_list


result = find_prime_list_under_number(input)
print(result)