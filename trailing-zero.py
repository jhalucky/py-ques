class Solution:
    def trailingZeroes(self, n):
        #code here 
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
    

s1 = Solution()
s1.trailingZeroes(7)