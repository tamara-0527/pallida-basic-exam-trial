# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

list_of_number = [1, 2, 3, 6, 8, 9, 11]
odd_number = []

#def odd_filter(odd_number):
number = 0 
for i in list_of_number:
    if number % 2 != 0:
        odd_number.append(i)
    number += 1
print(odd_number)
#print(odd_filter(odd_number))          

# L = [1, 2, 3, 4, 5, 6, 7]
# li = []
# count = 0
# for i in L:
#     if count % 2 == 1:
#         li.append(i)
#     count += 1   
# print(li)