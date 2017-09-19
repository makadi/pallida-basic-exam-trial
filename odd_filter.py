# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]



a = [1, 2, 3, 4, 5]

def odd_filter(a):
    for x in a:
        if x % 2 != 0:
            print [x]


odd_filter(a)