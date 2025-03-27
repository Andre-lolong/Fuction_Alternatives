# create a function
# check if the beginning is a space 
# remove the space
# print the output
def lstrip_alternative(text):
    i = 0
    while i < len(text) and text[i].isspace():
        i += 1
    return text[i:]

string = input("Enter something: ")
lstripped = lstrip_alternative(string)
print(lstripped)