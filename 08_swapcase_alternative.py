# same as program number 3
# check for uppercase and lowercase
# get the ASCII number and shift uppercase to lowercase and lowercase to uppercase
# add all to the final result
def swapcase_alternative(text):
  result = ""
  for letter in text:
    if 'A' <= letter <= 'Z':
      result += chr(ord(letter) + 32)
    elif 'a' <= letter <= 'z':
      result += chr(ord(letter) - 32)
    else:
      result += letter
  return result

text = input("Enter something: ")
swapcase = swapcase_alternative(text)
print(swapcase)
