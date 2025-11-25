def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
        if dp[target]:
            return True
    return dp[target]

def coinChange(coins, amount):

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0 

    for i in range(1, amount + 1):
 
        for coin in coins:

            if coin <= i:
   
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1

def maxSubArray(nums):
    def helper(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2

        left_max = helper(left, mid)
        right_max = helper(mid + 1, right)
        cross_max = cross_sum(left, mid, right)

        return max(left_max, right_max, cross_max)
    
    def cross_sum(left, mid, right):
        left_sum = 0
        max_left = float('-inf')
        for i in range(mid, left - 1, -1):
            left_sum += nums[i]
            max_left = max(max_left, left_sum)
        right_sum = 0
        max_right = float('-inf')
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            max_right = max(max_right, right_sum)
        
        return max_left + max_right
    
    return helper(0, len(nums) - 1)