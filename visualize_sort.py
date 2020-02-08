"""
Dohyun Lee
April 10th, 2019
A program that displays a visualization of how one particular
sorting algorithm works
"""
import random
def main():
    print("Welcome to Selection Sort!")
    print()
    n = int(input("Enter the size of the list: "))
    while n < 1:
        n = int(input("Enter the size of the list: "))
    lst = []
    for i in range(n):
        x = random.randint(1,15)
        lst.append(x)
    print("Our original list is: %s" % (lst))
    print()
    for i in range(len(lst)):
        print("*" * lst[i], "--", lst[i])
    selectionSort(lst)

def selectionSort(lst):
    """
    purpose: sorts a list of integers
    parameters: a list of integers in random order
    returns: none
    """
    for i in range(len(lst)-1,0,-1):
       max = 0
       newLst = []
       for location in range(0,i+1):
           newLst.append(lst[location])
           if lst[location]>lst[max]:
               max = location
       print("The maximum value in %s is %s" % (newLst, lst[max]))
       temp = lst[i]
       lst[i] = lst[max]
       lst[max] = temp
       if int(lst[i]) > int(lst[max]):
           print("Swap %s and %s" % (lst[i], lst[max]))
       else:
           print("No change")
       print()
       input("Hit enter to continue")
       print()
       for i in range(len(lst)):
           print("*" * lst[i], "--", lst[i])
    print()
    print("Selection sort complete!")


main()
