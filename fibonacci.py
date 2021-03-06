#recursion vs. iteration
#execute better algorithm
#https://github.com/turbocornball/Activity-2-Fibonacci.git

#timing two different ways of solving fibonacci sequence in python
#results are shown in a graph
#recursion vs iteration
#execution of a better algorithm


from matplotlib import pyplot as plt #importing matplotlib module for the graph
import time                          #for timing each function


#lists for storing the execution time on every input
recur_time = []
iter_time = []
angel_algo = []

#list for storing the range of input sizes
x = []

n = 5

#recursion function
def recur_fibo(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)

#iteration function
def iter_fibo(n):
    a,b=0,1
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

#efficient fibo function
def better_fibo(n):
    a,b=0,1
    while b <= iter_fibo(n):
        a,b=b,a+b


#loop for generating input sizes starting from size 5
#limited the size to 30 because my pc would take long to run
#the input size more than 30
while n < 30:
    n+=5
    x.append(n)

    #calling and timing the recursion function
    past=time.time()
    (recur_fibo(n))
    recur_time.append(time.time()-past)

    #calling and timing the recursion function
    past=time.time()
    print(iter_fibo(n))
    iter_time.append(time.time()-past)

    #calling and timing the better algorithm
    past=time.time()
    (better_fibo(n))
    angel_algo.append(time.time()-past)

# Function to plot
plt.plot(x, recur_time)
plt.plot(x, iter_time)
plt.plot(x, angel_algo)
plt.title('Fibonacci\n' + '(Execution Time)')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.legend(["Recursion Time", "Iteration Time", "Better Algo"])
# function to show the plot
plt.show()


print(recur_time)
print(iter_time)
print(angel_algo)
