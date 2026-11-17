# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first): for this problem, we're supposed to find the position off two numbers
    #that add up to a target number. We can do this by using a dictionary to store the numbers we have seen so far and their indices. 
    # As we iterate through the list, we can check if the complement (target - current number) exists in the dictionary.
    #  If it does, we return the indices of the two numbers. If not, we add the current number and its index to the dictionary.
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i


def max_profit(prices):
    # Outline: when given the stock prices we shoould find the largest positive differnce between a later selling price and an earlier buying price. We can do this by keeping track of the minimum price seen so far and the maximum profit we can achieve. As we iterate through the list of prices, we update the minimum price and calculate the potential profit for each price. If the potential profit is greater than the current maximum profit, we update the maximum profit.
    # we can do this by initializing two variables: `min_price` to zero and `max_profit` to 0. 
    # Then, we iterate through the list of prices. For each price, we update `min_price` if the current price is lower than `min_price`.
    #  We then calculate the maximum profit by subtracting `min_price` from the current price. 
    # If this maximum profit is greater than `max_profit`, we update `max_profit`.
    #  Finally, we return `max_profit`.
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
   
    return max_profit


def max_subarray(nums):
    # Outline: we're supposed to find the slice of the array that has the largest sum. 
    # we can use a nested loop to iterate through all possible subarrays and calculate their sums, keeping track of the maximum sum found.
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
