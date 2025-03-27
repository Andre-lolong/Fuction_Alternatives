# create a function
# capitalize the first and lower the others
# display
def capitalize_manual(text):
  if text:
    return text[0].upper() + text[1:].lower()
  return text