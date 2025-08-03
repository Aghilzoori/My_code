def zakhireh_etlaat():
    name = input("نام دانش اموز ")
    talfan = input("شماره تلفن")
    gmail = input("ایمیل دانش اموز ")

    sabat = f"نام : {name}\n شماره دانش اموز  : {talfan}\n جیمیل دانش اموز  : {gmail}\n{"--" * 50}"
    try:
        with open("contacts.txt", 'a', encoding="utf-8") as file:
            file.write(sabat)
            print("با موفقیت ثبت شد ")
        with open("contacts.txt", 'r', encoding="utf-8") as file:
            text = file.read()
            print(text)
        print("محتوا ")
    except FileNotFoundError:
        print("فایل وجود ندارد")
    except PermissionError:
        print("خطا ")