"""
#Teminijesu Titus Adewunmi
#Homework 1 CS 325
#4/12/2021
"""
import numpy as np #to get random number
import random       #to get random number
import time        #to find the running time

"""
Function: Megrge sort
about: it takes the date, splits them into and sorts them
input: fileName_arr is passed into it
output: none
"""
# mostly reused from cs 261 winter term 
def mergeSort(fileName_arr):
    if len(fileName_arr) > 1:
      i = j = k = 0
      middle = len(fileName_arr)//2
      left = fileName_arr[:middle]
      right = fileName_arr[middle:] 
      mergeSort(left)
      mergeSort(right)
      while  j < len(right) and i < len(left):
         if left[i] < right[j]:
            fileName_arr[k] = left[i]
            i += 1
         else:
            fileName_arr[k] = right[j]
            j += 1
         k += 1
      while i < len(left):
         fileName_arr[k] = left[i]
         i += 1
         k += 1
      while j < len(right):
         fileName_arr[k] = right[j]
         j += 1
         k += 1


"""
Function:main
about: it opens the news file, reads the data then calls merge sort
input: none
output: time taken to sort
"""
def main():
   n = 1000
   fileName_arr = [] * n

   print("size time")

   for x  in range(12):
      start = time.time()
      fileName_arr = np.random.randint(0, 10000, n)
      mergeSort(fileName_arr)
      end = time.time()
      mergeRuntime = end - start
      print(n, mergeRuntime)
      n += 1000
    


if __name__ == "__main__":
   main()
