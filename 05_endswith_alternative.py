# create a function
# check if it ends with the given suffix
# return true if yes and false if not
def endswith_alternative(text, suffix):
    text_len = len(text)
    suffix_len = len(suffix)

    if suffix_len > text_len:
        return False

    if text[text_len - suffix_len:] == suffix:
        return True
    else:
        return False