#Import Libriaries
import random


#Create Variables/Sets
list = []


#Add to Sets
for i in range(100):
    number = random.randint(1, 100)
    list.append(number)


"""
for i in range(100):
    list.append(i)

 """



#Display set With desired format
print("Unsorted List (Items Only): ")


#In this case
#numbers is the index number
#lists is the value stored at that index
#list is the actual list
for numbers, lists in enumerate(list):

    #Compares current index to the last index available in the list
    if numbers == len(list) - 1:
        print(lists, end="")
        break

    print(lists, end=",")



print()
print()
print("Sorted List (Items Only): ")


list.sort()

for numbers, lists in enumerate(list):

    if numbers == len(list) - 1:
        print(lists, end="")
        break

    print(lists, end=",")