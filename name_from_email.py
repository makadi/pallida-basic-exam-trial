# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter



# a = "zoltan.makadi@gmail.com"

b = input("Add your e-mail address here: ")

def splitter(email):

    full_name = email.split("@")[0]
    first_name = full_name.split(".")[0]
    last_name = full_name.split(".")[1]
    
    print(first_name.capitalize() + " " + last_name.capitalize())
    
splitter(b)