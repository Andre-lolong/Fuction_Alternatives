# create a function
# get the text and sapces from both sides
# add the spaces to both sides to make sure the text is in the center
# display
def center_alternative(text, width):
    text_len = len(text)
    if text_len >= width:
        return text

    space = width - text_len
    left_space = space // 2
    right_space = space - left_space

    return " " * left_space + text + " " * right_space