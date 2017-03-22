from __future__ import division
import random
import sympy

available = {896: 126126114111032101108267893162, 145: 126126114111032101108037789929, 66: 126126114111032101108033286850, 613: 126126114111032101108133329321, 545: 126126114111032101108112130729, 780: 126126114111032101108195947474, 602: 126126114111032101108129731474, 983: 126126114111032101108292268741, 988: 126126114111032101108294920946, 431: 126126114111032101108082173125}
#In a real time system the available dictionary will be filled with the data obtained from the different nodes.

recover = [ [k,v] for k, v in available.items() ]
# provision to select data to recover based on the network latency and traffic on each node.

A = []
B = []
rand = []
X = sympy.Symbol('X')
n = random.randint(0, 9)
if(n <4 ):
    # if the number of data bits available is less than 3 the system will be incapable of recovering the data.
    print ("The system is currently incapable of recovering your data. Please try again later.")
else:
    for i in range(0,3):
        rand = random.choice(recover)
        x = rand[0]
        y = rand[1]

        A.append([x])
        B.append([y])
        recover.remove(rand)

    print(A,B)
    
    # In = I-a(all except an)/an-a(all except an)
    I0 = sympy.solve(sympy.solve(X-A[1])(X-A[2])/((A[0]-A[1])(A[0]-A[2])))
    I1 = sympy.solve(sympy.solve(X-A[0])(X-A[2])/((A[1]-A[0])(A[1]-A[2])))
    I2 = sympy.solve(sympy.solve(X-A[1])(X-A[0])/((A[2]-A[1])(A[2]-A[0])))

    #result is recieved as summation of all bnIn
    result = sympy.solve((B[0](I0))+(B[1](I1))+(B[2](I2)))
    print (result)






