import random
piam0 = [
    "افرین تونستی درست بگی ",
    "بعد تلاش های زیاد درست گفتی ",
    "خیلی عالی بود بعد تلاش های زیاد",
    "اوه بنازم تونستی درست بگی "
]
piam1 = [
    "اوه نه نزدیک بود ",
    "دوباره تلاش کن ",
    "تو میتونی ",
    "بعد تلاش های زیاد جواب درست پیدا میکنی پس بیشتر تلاش کن "
]
while True:
    try:
        vrodi = int(input("عدد خود را وارد کنید : "))
        bot = random.randint(a=0, b=20)
        if vrodi == bot:
            piam_random0 = random.choice(piam0)
            print(f"{piam_random0} {bot}")
            break
        elif vrodi > bot:
            piam_random1 = random.choice(piam1)
            print(f"{piam_random1} {bot}")
        elif vrodi < bot:
            piam_random2 = random.choice(piam1)
            print(f"{piam_random2} {bot}")
    except ValueError:
        print("لطفا فقط عدد وارد کنید ")