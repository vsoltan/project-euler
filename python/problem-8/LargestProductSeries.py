# version 1.0
# author vsoltan

class LargestProductSeries():
    def findLargestProductSeries(list, probe):
        largest_product = 0
        list_given = str(list)
        for x in range(0, len(list_given) - probe + 1):
            new_product = 1
            for y in range(0, probe):
                new_product = new_product * int(list_given[x + y])
            if new_product > largest_product:
                largest_product = new_product
        return largest_product
