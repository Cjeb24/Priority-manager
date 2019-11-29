#Code to Run schedulers (FCFS,SJF,Priority,RR)

import csv
from pprint import pprint
def getprocesses(filename):
    processlist = []
    with open(filename, newline='') as csvfile:
        processreader = csv.reader(csvfile, )
        for line in processreader:
            processlist.append(tuple(line))
    return processlist

def fixer(myprocs):
    fixed=[]
    for i in myprocs:
        fixed.append([i[0], int(i[1].replace(" ", "")), int(i[2].replace(" ", ""))])
    return fixed
    
def FCFS(lst):
    start = 0
    print("FCFS")
    for i in lst:
        print(i[0], start, i[2]  )
        start +=  i[2]
def SJF(lst):
    temp = lst[:]
    temp2=[]
    start = 0
    while temp:
        a = (temp[0])[2]
        p = 0
        for i in range(len(temp)):
            if (temp[i])[2] < a:
                a = (temp[i][2])
                p = i
        temp2.append(temp[p])
        temp.remove(temp[p])
    print("SJF")
    for j in temp2:
        print(j[0], start, j[2]  )
        start +=  j[2]
def priority(lst):
    temp = lst[:]
    temp2=[]
    start = 0
    while temp:
        a = (temp[0])[1]
        p = 0
        for i in range(len(temp)):
            if (temp[i])[1] < a:
                a = (temp[i][1])
                p = i
        temp2.append(temp[p])
        temp.remove(temp[p])
    print("Priority")
    for j in temp2:
        print(j[0], start, j[2]  )
        start +=  j[2]
def RR(lst):
    temp = lst[:]
    start = 0
    print("RR:")
    while temp:
        for i in temp:
            if i[2] >= 10:
                print(i[0], start, i[2])
                i[2] -= 10
                if i[2] == 0:
                    temp.remove(i)
                start +=10
            else:
                start += i[2]
                print(i[0], start, i[2])
                temp.remove(i)
              
    
if __name__ == '__main__':
    myprocs = getprocesses('a5.csv')
    pprint(myprocs)
    fixed = fixer(myprocs)
    FCFS(fixed)
    SJF(fixed)
    priority(fixed)
    RR(fixed)
