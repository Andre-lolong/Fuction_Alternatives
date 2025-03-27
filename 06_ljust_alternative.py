# create a functiom
# choose width to be justified
# add it to the text
# display
def ljust_manual(text, width):
    text_len = len(text)
    if text_len >= width:
        return text

    spaces_to_add = width - text_len
    return text + " " * spaces_to_add

text = input("Enter a text: ")
spaces = int(input("Enter how many space you want: "))
print(ljust_manual(text, spaces))