"""
#Teminijesu Titus Adewunmi
#Homework 1 CS 325
#4/12/2021
"""

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
      #print(line)
      insertSort(line)
      print(line)


if __name__ == "__main__":
   main()
   