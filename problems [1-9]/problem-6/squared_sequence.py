def squared_sequence(x):
    squared_sum = list()
    for i in range(1, x + 1):
        squared_number = i ** 2
        squared_sum.append(squared_number)
    return sum(squared_sum)


def square_of_sum(x):
    return (x * (x + 1) / 2) ** 2


if __name__ == '__main__':
    print(square_of_sum(100) - squared_sequence(100))
