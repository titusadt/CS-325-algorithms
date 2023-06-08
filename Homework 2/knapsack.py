import numpy as np
import random
import time


#Using pseudocode from module 3
"""
Function: knapsackDP()
parameters: N, P, W, M
About: this function takes in values, calulates the max and returns them it does this recursively by having a base case
"""
#Recurvise implmentation
def knapsack_rec(n, W, val, wt):
    #base case
    if(n==0 or W==0):
        return 0

    if wt[n-1] > W :
        return knapsack_rec(n-1, W, wt, val)
    else:
        return max(val[n-1] + knapsack_rec(n-1, W-wt[n-1], wt, val), knapsack_rec(n-1, W, wt, val))

#dynamic implementation adapted from in class pseudocode
"""
Function: knapsackDP()
parameters: N, P, W, M
About: this function takes in values, calulates the max and returns them
"""
def knapsackDP(n, W, val, wt):
    

    T = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build the table
    for i in range(n + 1):
        for w in range(W + 1):
            if w == 0 or i == 0:
                T[i][w] = 0
            elif wt[i-1] <= w:
                T[i][w] = max(val[i-1] + T[i-1][w-wt[i-1]],  T[i-1][w])
            else:
                T[i][w] = T[i-1][w]
  
    return T[n][W]
  


"""
Function: main()
Parameters: none
About: This function reads all of the information from the file and prints out the currect values
"""
def main():
    val =[]
    wt = []

    #getting random values for val and wt
    val = np.random.randint(1, 100, 200)
    wt = np.random.randint(1, 15, 100)

    #assignin values for W and n
    W = 100
    n = 10
    for x in range(6):
        #REC TIME
        start = time.time()
        rec_val = knapsack_rec(n, W, val, wt)
        end = time.time()
        recTime = end -start
        
        #DP TIME
        startDP = time.time()
        dp_val = knapsackDP(n, W, val, wt)
        endDP = time.time()
        dpTime = endDP -startDP
        print("N = ", n, "W =", W, "Rec time=", recTime, "DP Time = ", dpTime, "Rec Max =", rec_val, "DP max = ", dp_val)
        n+=5
if __name__ == "__main__":
    main()
