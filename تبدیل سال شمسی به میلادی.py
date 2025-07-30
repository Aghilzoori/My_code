while True:
    try:
        roze, mah, sal = input().split()
        roze = int(roze)
        mah = int(mah)
        sal = int(sal)
        if mah >= 10 and roze >= 11:
            print(sal + 622)
        else:
            print(sal + 621)
    except ValueError:
        print("مقادیر را به ترتیب وارد کنید روز ماه سالذ ")