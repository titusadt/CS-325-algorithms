"""
Function: knapsackDP()
parameters: N, P, W, M
About: this function takes in values, calulates the max and returns them
"""

def knapsackDP(N, P, W, M):
    #assign the spaces for M and N to K
    K = [[0 for x in range(M + 1)] for x in range(N + 1)]
    
    # Build table K[][] in bottom up manner
    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif W[i-1] <= j:
                K[i][j] = max(P[i-1] + K[i-1][j-W[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    
    # list of items we will return
    res = []  
    
    i = N
    j = M

    # j is the weight and t is the index
    while(i > 0 and j > 0):

        if K[i][j] != K[i-1][j]:
            res.append(i-1)
            j = j - W[i - 1]
        i -= 1

    return res
    
"""
Function: main()
Parameters: none
About: This function reads all of the information from the file and prints out the currect values
"""

def main():
   
    fileName = open("shopping.txt", "r")
    #reading the first line of the file
    T = int(fileName.readline())
    
    for test_cases in range (T):
        #reading the second line of the file
        print("Test Case: ", test_cases+1)
        N = int(fileName.readline())
        
        P =[]
        W =[]

        for i in range (N):
            #reading the values for price and weight
            content = fileName.readline()
            [p, w] = [int(j) for j in content.split(" ")]
            P.append(p)
            W.append(w)
        
        
        maxPrice =0
        #reading the number of family members
        F =int(fileName.readline())
        list_of_items = []

        for k in range(F):
            #reading the max weight
            M = int(fileName.readline())
            arr = knapsackDP(N, P, W, M)

            list_of_items.append(arr)

            for item in arr:
                #calculating the maximum price
                maxPrice += P[item]

        print("Total Price: ", maxPrice)

        #loop to properly print the objects that each member of the  family carried 
        for l in range(len(list_of_items)):
            print(l+1,": ", end=' ',sep='')
            for m in range(len(list_of_items[l])):
                print(list_of_items[l][-m-1]+1, end=' ')
            print()




if __name__ == "__main__":
    main()








"""

def knapsackDP(N, P, W, M):
    K = [[0 for x in range(M + 1)] for x in range(N + 1)]
  
    # Build table K[][] in bottom up manner
    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif P[i-1] <= j:
                K[i][j] = max(W[i-1] + K[i-1][j-P[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    res = K[N][M]
    print(res)
    j = M 
    t = N

    while(t > 0 and j > 0):
        if res <= 0:
            break
        if res == K[t-1][j]:
            t -= 1
            continue
        else:
              # This item is included.
            print(P[t - 1])
            res = res - P[t - 1]
            j = j - W[t - 1]
    return K[t][j]
    
def main():
    P =[]
    W =[]
    fileName = open("shopping.txt", "r")
    #reading the first line of the file
    T = int(fileName.readline())

    for test_cases in range (T):
               #reading the second line of the file
        print("Test Case: ", test_cases+1)
        N = int(fileName.readline())
        for i in range (N):
            content = fileName.readline()
            [p, w] = [int(j) for j in content.split(" ")]
            P.append(p)
            W.append(w)
        maxPrice =0
        F =int(fileName.readline())

        for k in range(F):
            M = int(fileName.readline())
            maxPrice = maxPrice + knapsackDP(N, P, W, M)
        
        print("Total Price: ", maxPrice)


if __name__ == "__main__":
    main()

"""