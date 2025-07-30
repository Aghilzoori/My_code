from googlesearch import  search
from bs4 import BeautifulSoup
import requests
from dick_kalamat import list_kalamat
import time


kolmat_chat = ['خوبی', 'سلام', 'چخبرا', 'سلام چطوری', '', '', '', '', '']
jomleh = []
ze_kolmat = []
#  حلقه برسی کلمه کاربر و بسیاری از عملیات های دیگر


while True:
    karbar_verodi = input('شما: ')


    taqsim_kolmat = karbar_verodi.split()
    for taqsim in taqsim_kolmat:
        if taqsim in kolmat_chat:
            jomleh.append(list_kalamat[taqsim])
            print(jomleh)
        else:
            ze_kolmat.append(taqsim)

    tabadil_rashteh = " ".join(ze_kolmat)
    try:
        for i, x in enumerate(search(tabadil_rashteh, num_results=5)):
            try:
                ze_link = requests.get(x)
                try:
                    if ze_link.status_code == 200:
                        ejra = time.perf_counter()
                        ze_html = BeautifulSoup(ze_link.text, features='html.parser')
                        html_article = ze_html.find("article").get_text(strip=True)
                        html = BeautifulSoup(html_article, features='lxml')
                        for tag in html(['script', 'style', 'meta', 'link']):
                            tag.decompose()
                        estekharaj = ' '.join(html.stripped_strings)
                        print(estekharaj)
                        print("منبع", x)
                    else:
                        continue
                except Exception:
                    continue
            except requests.exceptions.RequestException:
                continue
    except Exception:
        print("خطا در بر قراری ارتبات اینترنت خود را برسی کنید")
    ze_kolmat.clear()