class Solution:
    def printPattern(self, n):
        self.n = n
        #Code here
        for i in range(1,n+1):
            if i == 1 or i == n:
                print('*' * i)
            else:
                print('*' + ' '* (i-2) + '*')
                
n1 = Solution()
n1.printPattern(5)
