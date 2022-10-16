import timeit


def sum_of_digits(number: int) -> int:
    sum_digits = 0
    while number:
        sum_digits += number % 10
        number //= 10
    return sum_digits


def customers_by_groups(n_customers: int, n_first_id: int = 0) -> dict[int: int]:
    """function return dictionary where key equals group and value equals amount of customers in group"""
    customers_groups = dict()
    for i in range(n_first_id, n_customers + n_first_id):
        group = sum_of_digits(i)
        # equals true if element with such key does not exist:
        if not customers_groups.get(group):
            customers_groups[group] = 1
        else:
            customers_groups[group] += 1
    return customers_groups


if __name__ == '__main__':
    assert(customers_by_groups(1) == {0: 1})
    assert(customers_by_groups(10) == {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    assert(customers_by_groups(27) == {0: 1, 1: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 2, 10: 1})
    assert(customers_by_groups(1, 0) == {0: 1})
    assert(customers_by_groups(13, 2) == {1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})
    first_argument = 13215
    second_argument = 134
    num_of_iter = 10
    print(timeit.timeit('customers_by_groups(first_argument, second_argument)', number=num_of_iter, globals=globals()))
