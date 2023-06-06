def uppercase(str):
    for c in str:
        ascii_value = ord(c)
        if ascii_value >= 97 and ascii_value <= 122:
            uppercase_char = chr(ascii_value - 32)
        else:
            uppercase_char = c
        print("{}".format(uppercase_char), end="")
    print()

