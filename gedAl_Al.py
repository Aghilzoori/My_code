class BarnamehRizi:
    def __init__(self):
        self.list_kar = []
    def list(self, kar):
        self.list_kar.append(kar)
        return self.list_kar
    def delete_kar(self, hz_kar):
        if hz_kar in self.list_kar:
            self.list_kar.remove(hz_kar)
            return self.list_kar
        else:
            return "کار نام برده شده داخل لیست وجود ندارد "

p1 = BarnamehRizi()
print("برای استعلام لیست کلمه لیست را وارد کید وبرای حذف یک فعلایت از برنامه زمانی کلمه حذف را وارد کنید ")
while True:
    kar_ha = input("...").upper()

    if kar_ha == "لیست":
        print(p1.list_kar)
    elif kar_ha == "حذف":
        print(p1.list_kar)
        hz_kar = input("برای حذف یکی از کار ها از لیست بالا ان را نام ببرید ")
        print(p1.delete_kar(hz_kar))
    elif kar_ha not in  p1.list_kar:
        print(p1.list(kar_ha))