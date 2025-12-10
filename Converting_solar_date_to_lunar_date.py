import time

ERROR = "مقادیر را به ترتیب وارد کنید: روز ماه سال"
GUIDE = "تاریخ خود را در کادر زیر وارد کنید به ترتیب روز ماه سال، مثال: 10 3 1389"

def time_in_text(text):
    for char in str(text):
        print(char, end='', flush=True) # هر حرف بلافاصله چاپ می‌شود
        time.sleep(0.3)
    print()

# نمایش راهنما
time_in_text(GUIDE)

while True:
    try:
        time_in_text("روز ماه سال")
        day, month, year = input("-> ").split()
        day = int(day)
        month = int(month)
        year = int(year)

        if month >= 10 and day >= 11:
            result = year + 622
        else:
            result = year + 621

        time_in_text(result)

    except ValueError:
        time_in_text(ERROR)
