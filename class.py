class BasicMaths:
    def factorial(self,x):
        fact=1
        for i in range(x,1,-1):
            fact*=i
        print("fact is "+str(fact))


num1 = BasicMaths()
num1.factorial(5)
