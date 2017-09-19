# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

list_of_number = [1, 2, 3, 6, 8, 9, 11]
odd_number = []

def odd_filter():
    number = 0 
    for i in list_of_number:
        if not i % 2 == 0:
            odd_number.append(i)
        i += 1
    print(odd_number)

odd_filter()          

# L = [1, 2, 3, 4, 5, 6, 7]
# li = []
# count = 0
# for i in L:
#     if count % 2 == 1:
#         li.append(i)
#     count += 1   
# print(li)