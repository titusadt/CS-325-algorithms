"""
#Teminijesu Titus Adewunmi
#Homework 1 CS 325
#4/12/2021
"""

"""
Function: Megrge sort
about: it takes the date, splits them into and sorts them
input: fileName_arr is passed into it
output: none
"""

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
# merge sort mostly reused from cs 261 winter term and

"""
Function:main
about: it opens the news file, reads the data then calls merge sort
input: none
output: sorted array
"""
def main():
   fileName = open("data.txt", "r")

   fileName_arr = []
   for line in fileName.readlines():
      line = line.split(' ')
      # cast elements of line to int or float
      for i in range(len(line)):
         line[i] = int(line[i])

      fileName_arr.append(line)

   for line in fileName_arr:
      mergeSort(line)
      print(line)


if __name__ == "__main__":
   main()
   