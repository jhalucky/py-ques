class Solution:
    def factorial (self, n):
        # code here
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1
        return fact