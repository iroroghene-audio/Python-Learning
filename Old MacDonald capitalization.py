def old_macdonald(string):
    modified_string = []
    index = 0

    for char in list(string):
        if index == 0 or index == 3:
            modified_string.append(char.upper())
        else:
            modified_string.append(char)
        index += 1
    return ''.join(modified_string)


checker = old_macdonald('macdonald')

print(checker)