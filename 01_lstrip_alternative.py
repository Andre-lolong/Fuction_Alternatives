def remove_leading_spaces(text):
    i = 0
    while i < len(text) and text[i].isspace():
        i += 1
    return text[i:]

my_string = input("Enter something: ")
result = remove_leading_spaces(my_string)
print(result)