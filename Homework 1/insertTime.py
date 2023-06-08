"""
#Teminijesu Titus Adewunmi
#Homework 1 CS 325
#4/12/2021
"""
import numpy as np 
import random  #random number generator
import time    #to get the time

"""
Function: insertSort
about: it sorts data
input: the data that needs to be sorted 
output: none
"""
def insertSort(fileName_arr):
    for i in range(len(fileName_arr)):
        insert = fileName_arr[i]
        j = i-1
        while j >= 0 and insert < fileName_arr[j] :
                fileName_arr[j + 1] = fileName_arr[j]
                j -= 1
        fileName_arr[j + 1] = insert


"""
Function:main
about: it opens the news file, reads the data then calls insert sort
input: none
output: the time taken to sort
"""np.random.randint(0, 10000, n)
def main():
    n = 1000
    fileName_arr = [] * n

    print("size time")
    for x in range(12):
        start = time.time()
        fileName_arr = 
        insertSort(fileName_arr)
        end = time.time()
        insertRuntime = end - start
        print(n, insertRuntime)
        n+=1000
    

if __name__ == "__main__":
   main()