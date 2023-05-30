from num2words import num2words

h = 5
m = 00


def time_in_words(h, m):

    while True:
        if m == 00:
            result = f"{num2words(h)} o' clock"
            break
        if m == 30:
            result = f"half past {num2words(h)}"
            break
        if m == 15:
            result = f"quarter past {num2words(h)}"
            break
        if m == 45:
            result = f"quarter to {num2words(h + 1)}"
            break
        if m < 30:
            result = f"{num2words(m)} minutes past {num2words(h)}"
            break
        if m > 30:
            l = num2words(60 - m).split('-')
            word = ""
            for i in l:
                word = word + i + " "
            result = f"{word}minutes to {num2words(h+1)}"
            break
    return result


print(time_in_words(h, m))
