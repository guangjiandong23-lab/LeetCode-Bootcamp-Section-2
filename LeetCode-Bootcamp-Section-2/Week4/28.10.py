
# 232. Implement Queue using Stacks
class MyQueue(object):

    def __init__(self):
        self.stackIn = []  # Input stack
        self.stackOut = []  # Output stack

    def push(self, x) -> None:
        self.stackIn.append(x)

    def pop(self)-> int:
         
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        
        return self.stackOut.pop()
        

    def peek(self) -> int:
        
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        
        return self.stackOut[-1]
        

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut
# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures): 
        n = len(temperatures)
        answer = [0] * n  
        stack = []  

        for i in range(n):
        
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  
                answer[prev_index] = i - prev_index 
            stack.append(i) 

        return answer
# 2327. Number of People Aware of a Secret
class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)  
        pre_sum = [0] * (n + 1)  
        MOD = 10**9 + 7
        
        dp[1] = 1
        pre_sum[1] = 1
        
        for i in range(2, n + 1):
            
            a = max(1, i - forget + 1)
            b = i - delay
            if b >= a:
                
                dp[i] = (pre_sum[b] - pre_sum[a - 1]) % MOD
            else:
                dp[i] = 0  
            
            
            pre_sum[i] = (pre_sum[i - 1] + dp[i]) % MOD
        
        
        a_final = max(1, n - forget + 1)
        total = (pre_sum[n] - pre_sum[a_final - 1]) % MOD
        return total
        