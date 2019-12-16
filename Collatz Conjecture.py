"""
The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n.
Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. 
If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture is that no matter what value of n, the sequence will always reach 1.
"""

x = int(input("Enter a Number:\n"))
step = 0

'''' Comment - (Loop for Finding The Whole sequence leading
 to 1 and number of steps involved)'''
while x != 1:
    if x%2 == 0:
        x= x/2
    else:
        x = 3*x +1
    print(x)
    step +=1

print("Number of steps involved are " + str(step))
