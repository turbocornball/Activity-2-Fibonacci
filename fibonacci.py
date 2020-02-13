from matplotlib import pyplot as plt
import time


recur_time = []
iter_time = []
x = []

n = 5
while n < 30:
    n+=5
    x.append(n)
    past=time.time()
    def Fibonacci(n): 
        if n<0: 
            print("Incorrect input") 
        # First Fibonacci number is 0 
        elif n==1: 
            return 0
        # Second Fibonacci number is 1 
        elif n==2: 
            return 1
        else: 
            return Fibonacci(n-1)+Fibonacci(n-2)
    
    (Fibonacci(n))
    recur_time.append(time.time()-past)
    #print("Recursion Execution Time: {} seconds".format(time.time()-past))


    def fibonacci(n): 
        past = time.time()
        a = 0
        b = 1
        if n < 0: 
            print("Incorrect input") 
        elif n == 0: 
            return a 
        elif n == 1: 
            return b 
        else: 
            for i in range(2,n): 
                c = a + b 
                a = b 
                b = c 
            return b 

    (fibonacci(n)) 
    iter_time.append(time.time()-past)
    #print("Iteration Execution Time: {} seconds" .format(time.time()-past))
    
# x-axis values 
#x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
#y = [10, 5, 8, 4, 2] 
  
# Function to plot 
plt.plot(x,recur_time) 
plt.plot(x,iter_time)
  
# function to show the plot 
plt.show() 

