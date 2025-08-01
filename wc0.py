def jabejayi( ):
    try:
        vorodi1, vorodi2 = input().split()
        text1 = vorodi1[-1]
        text2 = vorodi2[-1]
        text3 = vorodi1[:-1]
        text4 = vorodi2[:-1]
        return text4 + text1 + " " + text3 + text2
    except ValueError:
        return "فقط کلمه های کوتاه میتوانید وارد کنید "
print(jabejayi())

