def meme_format(text=None):
    if text == None:
        text = str(input(
            "\nCopy and paste text here or write your own and transform it into a beautiful meme!:\n\n"))

    count = 0
    for index, i in enumerate(list(text).copy()):
        if i.isalpha():
            if count == 1:
                text = text[:index] + i.upper() + text[index+1:]
                count -= 1
            else:
                text = text[:index] + i.lower() + text[index+1:]
                count += 1
        else:
            continue
    return text


# print("\n")
# print(meme_format("hello, my name is Bob. I like bob"))
