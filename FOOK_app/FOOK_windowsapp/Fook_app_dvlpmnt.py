from customtkinter import *
from PIL import Image
from googletrans import Translator
from deep_translator import GoogleTranslator


def traduzir():
    global idioma
    if idioma == "pt":
        titulo_label.configure(text=traducao_en)
        idioma = "en"
    else:
        titulo_label.configure(text=traducao_pt)
        idioma = "pt"


translator = Translator()
texto_orig = "Bem vindo ao FOOK v.01!"
idioma = "pt"
app = CTk()
app.geometry("500x400")
app.title('FOOK')
set_appearance_mode('dark')


# Configurar icone:
app.iconbitmap("D:/Estudo/programação/Python/curso/projects/Projects_/FOOK_app/FOOK_windowsapp/imagens/FOOK_icon/big_fookicon.ico")

# Configurar pesos para centralização responsiva
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)

# Imagens
imgd = Image.open('D:/Estudo/programação/Python/curso/projects/Projects_/FOOK_app/FOOK_windowsapp/imagens/FOOK _symbols/download_icon.png').resize((60,60))
ctk_imgd = CTkImage(dark_image=imgd, light_image=imgd, size=(60,60))

imgs = Image.open('D:/Estudo/programação/Python/curso/projects/Projects_/FOOK_app/FOOK_windowsapp/imagens/FOOK _symbols/search_icon.png').resize((60,60))
ctk_imgs = CTkImage(dark_image=imgs, light_image=imgs, size=(40,40))

imgr = Image.open("D:/Estudo/programação/Python/curso/projects/Projects_/FOOK_app/FOOK_windowsapp/imagens/FOOK _symbols/read_icon.png").resize((60,60))
ctk_imgr = CTkImage(dark_image=imgr, light_image=imgr, size=(60,60))

imgl = Image.open("D:/Estudo/programação/Python/curso/projects/Projects_/FOOK_app/FOOK_windowsapp/imagens/FOOK _symbols/lang_icon.png").resize((60,60))
ctk_imgl = CTkImage(dark_image=imgl, light_image=imgl, size=(40,40))

# Label centralizada
titulo_label = CTkLabel(app, text=texto_orig, font=CTkFont(size=24, weight="bold"), text_color='red')
titulo_label.grid(row=0, column=0, columnspan=2, pady=20)

# Tradução prévia
traducao_en = GoogleTranslator(source='pt', target='en').translate(texto_orig)
traducao_pt = texto_orig  # já tens


# Botões
btn_download = CTkButton(app, text=None, fg_color='#F41301', hover_color="#8D0E0E", width=80, height=80, image=ctk_imgd)
btn_read = CTkButton(app, text=None, fg_color='#F41301', hover_color="#8D0E0E", width=80, height=80, image=ctk_imgs)
btn_search = CTkButton(app, text=None, fg_color='#F41301', hover_color="#8D0E0E", width=80, height=80, image=ctk_imgr)
btn_lang = CTkButton(app, text=None, fg_color="#F41301", hover_color="#8D0E0E", width=80, height=80, image=ctk_imgl, command=traduzir)


btn_download.grid(row=1, column=0, padx=20, pady=20)
btn_search.grid(row=1, column=1, padx=20, pady=20)
btn_read.grid(row=1, column=0, columnspan=2, pady=20)
btn_lang.grid(row=2, column=0, columnspan=1,pady=20)
app.minsize(width=400,height=300)
app.maxsize(width=800, height=600)
app.mainloop()




