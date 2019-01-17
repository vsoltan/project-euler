# version 1.0
# author vsoltan

# largeNum is not passed to the calculate method in list form
# assuming that [0,9] are included

class LargeSum:
    def calculateLargeSum(largeNum):

        # create a sorted list

        cumulative_sum = 0
        largeNum = list(str(largeNum))
        largeNum.sort()

        ## remove zeroes

        index_one = largeNum.index('1')
        largeNum = largeNum[index_one::]

        for x in range(2, 10):
            index = largeNum.index(str(x)) if str(x) in largeNum else -1
            # if index < 0: continue
            cumulative_sum = cumulative_sum + (x - 1) * (index)
            largeNum = largeNum[index::]

        return cumulative_sum + 9 * len(largeNum)
