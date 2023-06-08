import numpy as np

"""
Parameters: list of sorted start times
Function: it returns the maximum number of activities and the list of those activities
"""
def greedy(id_start_finish):
    item = len(id_start_finish)
    store = []
    store.append(id_start_finish[0, 0])
    last_chosen_index = 0

    # for each of the remaining lines in id_start_finish, in order,
    for i in range(1, item):
        # if the activity on this line is compatible with the most recent chosen activity,
        # compatible: this (the ith) activity's finish time is <= the last chosen activity's start time
        if(id_start_finish[last_chosen_index, 1] >= id_start_finish[i, 2]):
        # then choose this activity.
            store.append(id_start_finish[i, 0])
            last_chosen_index = i

    print("Maximum number of activities = ", len(store))
    return store


"""
Parameters: none
Function: it reads the file and sorts the start times
"""
def main():


    with open("act.txt", "r") as fileName:
        #reading the total number of activities from the file
        output = 1
        for f in fileName:
            #going through all of the activities and storing the number and the times
            print("Set: ", output)
            activity_num =[]
            start_time = []
            finish_time = []
            for num in range(int(f)):
                content = fileName.readline()

                [active_num, start, finish] = [int(j) for j in content.split(" ")]
                #storing the separated number, start_time and finish_time
                activity_num.append(active_num)
                start_time.append(start)
                finish_time.append(finish)

             # sort id_start_finish in descending order of start times
            id_start_finish = np.array(list(zip(activity_num, start_time, finish_time))).astype(int)
            indices = np.argsort(id_start_finish[:, 1])[::-1]
            id_start_finish = id_start_finish[indices]

            item = len(id_start_finish)
            #call the function
            max = greedy(id_start_finish)[::-1]
            print(max)
            output +=1






if __name__ == "__main__":
   main()
