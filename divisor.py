class Solution:
    def print_divisors(self, n):
        # code here
        self.n = n
        i = 1
        while i<=n:
            if n%i == 0:
                print(i, end=' ')
            i+=1
        