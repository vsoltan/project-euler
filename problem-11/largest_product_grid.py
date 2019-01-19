"""dynamic method of finding the maximum product in a predefined grid"""


def find_largest_product(array, probe):
    largest_product = 0
    for i in range(0, array.shape[1] + 1 - probe):
        for j in range(0, array.shape[0] + 1 - probe):
            curr_product = calc_product(array, i, j, probe)
            largest_product = curr_product if curr_product > largest_product else largest_product
    return largest_product


def calc_product(array, row, col, probe):
    product = array[row][col]
    for i in range(1, probe):
        product = product * array[row + i][col + i]
    return product

# if __name__ == '__main__':
