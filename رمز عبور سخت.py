while True:
    ramz_obur = input("رمز عبور خود را وارد کنید : ")
    adad = any(chat.isalpha() for chat in ramz_obur)
    horof = any(chat.isdigit() for chat in ramz_obur)
    if ramz_obur == "خروج":
        print("اگه دوست داشتی بهترین رمز و امن ترین را پیدا کنیم بهم بگو ")
        break
    elif adad and horof:
        print("خیلی عالی رمز عبور شما تعید شده و میتوانید از ان داخل سایت ها استفاده کنید")
        print(ramz_obur)
    else:
        print("رمز عبور شما امن نیست و احتمال از بین رفتن ان خیلی زیاد هست ")