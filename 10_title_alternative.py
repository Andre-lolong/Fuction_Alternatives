# create a function
# capitalize each in the list of splitted text
# join and display
def title_alternative(text):
  return " ".join(word.capitalize() for word in text.split())

text = input("Enter something: ")
print(title_alternative(text))