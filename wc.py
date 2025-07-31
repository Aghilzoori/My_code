def miangin(list_adad):
    adad = sum(list_adad) / len(list_adad)
    return  "میاگین عداد", adad


zh_adad = []
while True:
    print("میانگین عادی که نیاز دارید پایین وارد کنید ")
    vorodi = input()
    try:
        for i in vorodi.strip().split():
            zh_adad.append(int(i))
        print(miangin(zh_adad))
        zh_adad.clear()
    except ValueError:
        print("فقط عداد ")