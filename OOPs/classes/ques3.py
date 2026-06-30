class Computation:

    def __init__(self):
        pass

    def Factorial(self,n):
        self.n = n
        fact = 1
        for i in range(1, self.n+1):
            fact*=i

        return fact
    
    def naturalSum(self, n):
        self.n = n
        sum = 0
        for i in range(1, self.n + 1):
            sum+=i

        return sum
    
    def testPrime(self, n):
        self.n = n
        for i in range(2, self.n):
            if self.n%i == 0:
                return f"{self.n} is not prime"
            else:
                return f"{self.n} is prime"
            

    def testPrims(self,n,k):
        self.n = n  
        self.k = k

        # fact_n = []
        # fact_k = []
        # for i in range(2,self.n):
        #     if self.n%i == 0:
        #         fact_n.append(i)
        
        # for j in range(2,self.k):
        #     if self.k%j == 0:
        #         fact_k.append(j)

        smaller = min(self.n,self.k)

        for i in range(2, smaller + 1):
            if self.n%i == 0 and self.k%i == 0:
                return False
            

        return True

            
    def tableMult(self,n):
        self.n = n
        table = ''
        for i in range(1, 11):
            table += f"{n * i}\n"

        return table
        
    def allTablesMult(self):
        table = ''
        for i in range(1,10):
            for j in range(1,11):
                table += f"{i * j}\n"
        return table



obj1 = Computation()
print(obj1.tableMult(2))
print(obj1.Factorial(5))
print(obj1.naturalSum(10))
print(obj1.testPrime(3))
print(obj1.testPrims(4,9))
# print(obj1.allTablesMult())

# n = int(input("Enter n: "))
# for i in range(1,11):
#     print(n*i)