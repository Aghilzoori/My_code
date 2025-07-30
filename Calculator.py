import re
 
while True:
    verodi = input()
    if verodi == "خروجی":
        print("خروج از ماشین حساب ")
    elif re.fullmatch(r"[0-9+\-*/(). ]+", verodi):
        try:
            natijeh = eval(verodi)
            print(natijeh)
        except ZeroDivisionError:
            print("خطا: تقسیم بر صفر مجاز نیست!")
        except:
            print("خطا: عبارت نامعتبر است!")
    else:
        print("خطا: فقط عملیات ریاضی مجاز است!") 
            
