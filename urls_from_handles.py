# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2"]

def urls_from_handles(a):
    b = "https://github.com/greenfox-academy/" + str(a[0])
    c = "https://github.com/greenfox-academy/" + str(a[1])

    d = [b, c]
    return d
print(urls_from_handles(names))