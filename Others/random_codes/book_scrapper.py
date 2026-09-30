import cloudscraper
from bs4 import BeautifulSoup
import time
import random
import requests


autor = input('Nome do Autor (não digite nada se nao souber) : ').strip()

book = input('Digite o Livro que deseja encontrar: ')
lang = input('Idioma do Livro: ')


#Identifica o idioma
identifygrp = {
    'eng' : [f'https://dokumen.pub/{book}.html', f'https://dokumen.pub/qdownload/{book}.html'],


    'pt' : [f'https://dlivros.com/livro/{book}', f'https://dokumen.pub/{book}.html' ]
}



# ---------------------    cria scraper 
def get_html(url):
    # Cria scraper com fingerprint de navegador real
    scraper = cloudscraper.create_scraper(
        browser={
            "browser": "chrome",
            "platform": "windows",
            "mobile": False
        }
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com"
    }

    # Tenta várias vezes (Cloudflare às vezes falha na 1ª tentativa)
    for tentativa in range(5):
        try:
            print(f"\nOn Url_:  {url}\nTry: {tentativa+1}") 
            r = scraper.get(url, headers=headers, timeout=15)

            # Se o Cloudflare devolver desafio
            if "Just a moment" in r.text or "Enable JavaScript" in r.text:
                print("Cloudflare bloqueou, tentando novamente...")
                time.sleep(random.uniform(2, 5))
                continue

            return r.text

        except Exception as e:
            print("Erro:", e)
            time.sleep(random.uniform(2, 5))

    return None



# ------------------    identifica se retorna algum erro
def geterr_0(url ,errorlist,soup,r):

    error_class = soup.find(class_="search search-no-results custom-background wp-embed-responsive header-full-width full-width-content genesis-breadcrumbs-visible genesis-footer-widgets-hidden" )

    meta = soup.find("meta", property="og:title")
    if meta:
        meta_get = meta.get("content", '' )

    if r.text in errorlist or error_class or '404' in r.url or r.status_code == 404 or meta and '404' in meta_get:
        print("Livro não existe")


    else:
        print("Livro existe\n")

    #print(r.url)
    #print(r.text)
    #print(r.status_code)

# ------------------------ apanha a requisição e chama o geterr_0
def get_req(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    r = requests.get(url)

    errorlist = ['404', 'Página Não Encontrada']

    soup = BeautifulSoup(html, "html.parser")
    r = requests.get(url)

    if not html:
        print("Não foi possível obter o HTML (Cloudflare muito forte).")
        exit()

    geterr_0(url=url,errorlist=errorlist,soup=soup,r=r)


# ------------------------ codigo principal
def center(srch=False):
    if lang in identifygrp and lang == 'eng':

        for x in range(len(identifygrp['eng'])):
            url = identifygrp['eng'][x]
            if not srch:
                url = url.replace(' ', '-')
                book_fixed = book.replace(' ', '-')
            else:
                url = url.replace(' ', '+')
                book_fixed = book.replace(' ', '+')
            print('Testando sem autor...')
            get_req(url)

            if autor != '' and len(autor) >= 4 :
                url1 = url.split(book_fixed)[0]
                if srch is True:
                    url = url1 + f"{book_fixed}+{autor}"
                else:
                    url = url1 + f"{book_fixed}-{autor}.html"
                print('Testando com autor...')
                get_req(url)

    elif lang in identifygrp and lang == 'pt':
        url = identifygrp['pt'][0]
        if srch is True:
            url = url.replace(' ','+')
        else:
            url = url.replace(' ', '-')
        get_req(url)

center()
####### Diz livro encontrado quando faço pesquisa no pt, resolver !!
# -----------  Pergunta ao utilizador se deseja fazer uma pesquisa 

searc = input('\nDeseja fazer pesquisa do Livro?\n>>> ')
if searc == '1':
    identifygrp = {
        'eng' : [f'https://oceanofpdf.com/?s={book}'],


        'pt' : [f'https://dlivros.com/Buscar?q={book}']
    }

    center(True)









