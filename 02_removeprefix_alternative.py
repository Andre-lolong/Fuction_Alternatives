# create a function 
# identify the main text and prefix
# if the prefix is in the sentence, remove the prefix
# print the text with removed prefix
def remove_prefix_manual(text, prefix):
  if text.startswith(prefix):
    return text[len(prefix):]
  return text

main = input("Enter the main text: ")
prefix = input("Enter a prefix: ")
print(remove_prefix_manual(main, prefix))