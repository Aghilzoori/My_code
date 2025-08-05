import re

#بخش فابل ها
file_verodi = 'log.server'
file_khroji = 'report.txt'
#ذخیره در فایل ها
taedad_kel_piameya = 0
taedad_noe = {"INFO": 0, "WARNING": 0, "ERROR": 0}
dasteh_bandi_ha = {
    "ورود کاربران": 0,
    "خطاهای سیستمی": 0,
    "هشدارهای ذخیره‌سازی": 0
}
#هشدار تمیز
hoshtar_ha = set()

#اسخراح فایل
with open(file_verodi, 'r', encoding='utf-8') as file:
    text = file.readlines()
for line in text:
    taedad_kel_piameya += 1
    #جوستجو نزدیک ترین تطابق‌. b برای تمیزی کار
    motabaght_dadan = re.search(r"\b(INFO|WARNING|ERROR)\b", line)
    if motabaght_dadan:
        #تطابق‌ گروه یک
        noe_piam = motabaght_dadan.group(1)
        taedad_noe[noe_piam] += 1
    #برسی
    if "User login" in line:
        dasteh_bandi_ha["ورود کاربران"] += 1
    if "Database" in line or "File" in line:
        dasteh_bandi_ha["خطاهای سیستمی"] += 1
        hoshtar_ha.add("بررسی اتصال پایگاه داده و سلامت فایل‌ها توصیه می‌شود.")
    if "disk" in line or "storage" in line:
        dasteh_bandi_ha["هشدارهای ذخیره‌سازی"] += 1
        hoshtar_ha.add("بررسی فضای دیسک و وضعیت ذخیره‌سازی توصیه می‌شود.")
#درصد شماری
def darsad(shmarsh):
    #تابع round برای گرد کردن هستش یک ریاضی بخون
    if taedad_kel_piameya:
        return round((shmarsh / taedad_kel_piameya) * 100, 2)
    else:
        return 0
with open(file_khroji, 'w', encoding='utf-8') as file:
    file.write(f"تعداد کل پیام‌ها: {taedad_kel_piameya}\n")
    file.write("آمار نوع پیام‌ها:\n")
    for msg_type in taedad_noe:
        file.write(f"  {msg_type}: {taedad_noe[msg_type]} پیام ({darsad(taedad_noe[msg_type])}%)\n")

    file.write("\nدسته‌بندی پیام‌ها:\n")
    for category in dasteh_bandi_ha:
        file.write(f"  {category}: {dasteh_bandi_ha[category]} پیام\n")

    file.write("\nپیشنهادات:\n")
    for rec in hoshtar_ha:
        file.write(f"  - {rec}\n")

# نمایش خلاصه در ترمینال
print(f"✅ پردازش کامل شد. تعداد کل پیام‌ها: {taedad_kel_piameya}")
for msg_type in taedad_noe:
    print(f"{msg_type}: {taedad_noe[msg_type]} پیام ({darsad(taedad_noe[msg_type])}%)")
print("📄 گزارش در فایل 'report.txt' ذخیره شد.")