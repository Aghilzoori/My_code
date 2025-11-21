import random

NUMBER = 8
passwords = []
pro_password = []

def Find_eight_letters():
    Save_output = []
    letter = list("qwertyuiopasdfghjklzxcvbnm")
    for _ in range(NUMBER):   
        Save_output.append(random.choice(letter))
    return ''.join(Save_output)

def Find_eight_numbers():
    # برای اطمینان از 6 رقم بودن و پر کردن با صفر در سمت چپ
    return str(random.randint(0, 999999)).zfill(6)

def Create_password():
    Letters = Find_eight_letters()
    Number = Find_eight_numbers()
    return f"{Letters}{Number}"

while True:
    ramz_obur = input("رمز عبور خود را وارد کنید : ")
    
    if ramz_obur == "استعلام رمز ها":
        print('\n'.join(passwords))
        continue
    
    if ramz_obur == "ساخت رمز":
        inputt = input("لطفا یک راهنما رمز بگویید به عنوان مثال رمز سایت کدیاد: ")
        if inputt:
            password = Create_password()
            while password in pro_password:
                password = Create_password()
            print(f"پسورد شما {password}")
            t = f"{password} : {inputt}"
            passwords.append(t)
            pro_password.append(password)
            continue
    
    if ramz_obur == "ساخت رمز شخصی":
        user_input = input("رمز عبور خود را بگویید: ")
        if user_input == "خروج":
            print("اگه دوست داشتی بهترین رمز و امن ترین را پیدا کنیم بهم بگو ")
            break
        
        adad = any(chat.isalpha() for chat in user_input)
        horof = any(chat.isdigit() for chat in user_input)
        
        if adad and horof:
            print("خیلی عالی رمز عبور شما تعید شده و میتوانید از ان داخل سایت ها استفاده کنید")
            print(user_input)
        else:
            print("رمز عبور شما امن نیست و احتمال از بین رفتن ان خیلی زیاد هست ")
        continue
    
    print("دستور نامعتبر! لطفا از 'ساخت رمز'، 'ساخت رمز شخصی' یا 'استعلام رمز ها' استفاده کنید.")
