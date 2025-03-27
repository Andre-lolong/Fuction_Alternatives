# create a functiom
# identify the letters
# if lowercase then return false and true if uppercase
def is_upper_manual(text):
  for char in text:
    if 'a' <= char <= 'z':
      return False
  return True
