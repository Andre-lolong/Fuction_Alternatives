# create a function
# check for capital letters
# get the ASCII number and shift uppercase to lowercase
# add all the lowercase to the final result
def lower_alternative(text):
  result = ""
  for letter in text:
    if 'A' <= letter <= 'Z':
      lowercase_letter = chr(ord(letter) + 32)
      result += lowercase_letter
    else:
      result += letter
  return result

text = input("Enter something with uppercase: ")
lowercase = lower_alternative(text)
print(lowercase)
