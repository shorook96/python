def longst(text):
    next = 1
    current = 0
    max = ""
    str = text[0]
    if (len(text) == 1):
        return text
    while current < len(text):
        if next == len(text):
            break
        str = text[current]
        while text[current] < text[next]:

            # print("i")
            str = str + text[next]
            current = next
            next = next + 1
            if len(max) < len(str):
                max = str
                # print(max)
            if next == len(text):
                break

        current = current + 1
        next = next + 1

    return max


print(longst("abcabcdef"))
# print("i")