def canSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


print(canSum(1005, [4, 6]))
