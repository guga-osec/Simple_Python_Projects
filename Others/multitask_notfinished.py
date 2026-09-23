# Este código tem como intenção ter multifunções para diversas situações

import subprocess
from colorama import Fore, Style, init
init()

def soes():
    print()
    Soesc = input(': W - Windows\n: L - Linux\n-->> ').lower()
    print()
    return Soesc


def netsee(nest,wla,shw,netw,mod, s):

    result = subprocess.run(
        [nest, wla, shw, netw, mod],
        capture_output=True,
        text=True
    )
    print(Fore.GREEN + '\n','-' * 40 + Style.RESET_ALL )
    if s is False:
        print(result.stdout)
    else:
        for lines in result.stdout.splitlines():
            if 'SSID ' in lines:
                print(lines)
    
    print(Fore.GREEN + '-' * 40 + Style.RESET_ALL +'\n')

def lerarq(arq, pal):
    try:
        with open(arq, "r", encoding="utf-8") as f:
            for numero_linha, linha in enumerate(f, start=1):
                if pal in linha:
                    print(f"Linha {numero_linha}: {linha.strip()}")
    except OSError:
        print()
        print('!! Coloque o caminho do arquivo certo !!')
        
def conct_net(ssid):
    intern_avail = subprocess.run(
    ["netsh", "wlan", "show", "profiles"],
    capture_output=True,
    text=True
)

    saida = intern_avail.stdout.strip()

    if intern_avail.returncode != 0:
        print("Erro ao executar netsh:")
        print(intern_avail.stderr)
    elif not saida:
        print("Nenhum perfil Wi-Fi encontrado ou permissões insuficientes.")
    else:
        cmd = f'netsh wlan connect name="{ssid}"'
        return cmd, saida
    




    
Soesc = soes()
menu = True
menuc = True
while menuc is True:
    if Soesc == 'w':
        while Soesc == 'w' and menu is not False:
            try:
                menu = int(input(': 1 - Ver Redes locais\n: 2 - Conectar se a uma rede já guardada\n: 3 - Pesquisar em um arquivo\n: 4 - Mudar SO\n: 5 - Sair\n>>> '))
            except ValueError:
                print('!ERRO! DIGITE APENAS Nºs inteiros\n')
                continue
            try:
                if menu == 1:
                    print()
                    esclh = int(input('---- Ver apenas SSID: 1\n---- Ver a infrastrutura toda: 2\n>>> '))
                    if esclh == 1:
                        netsee('netsh', 'wlan','show', 'networks', 'mode=Bssid', True)
                    elif esclh == 2:
                        netsee('netsh', 'wlan','show', 'networks', 'mode=Bssid', False)
                elif menu == 2:
                    
                    print()
                    print( Fore.BLUE + '-','/' * 40,'-' + Style.RESET_ALL + '\n')
                    saida_iab = conct_net('')[1]
                    print(saida_iab)
                    print()
                    ssid = input('Wifi Name: ').strip()
                    print()
                    cmd = conct_net(ssid)[0]
                    process = subprocess.run(cmd, shell=True, capture_output= True, text=True)
                    print('--- ' + process.stdout.splitlines()[0] + '\n')
                    print( Fore.BLUE + '-','/' * 40,'-' + Style.RESET_ALL + '\n')
                    print()
                elif menu == 3:
                    arq = input('Digite o caminho do arquivo:\n  <<>> ')
                    pala = input('Digite a palavra/Frase: ')
                    print( Fore.RED + '\n','+'* 30 + Style.RESET_ALL )
                    lerarq(arq,pala )
                    print( Fore.RED + '\n','+'* 30 + Style.RESET_ALL + '\n')

                    
                elif menu == 4:
                    Soesc = soes()
                elif menu == 5:
                    menu = False
                    menuc = False
                    break

            except NameError:
                continue
    elif Soesc == 'l':
        print('!! programa nao automizado para Linux !!\n')
        break
    else:
        print('-'*50 ,'\n!! ERRO !!\n___APENAS W/L ACEITOS___\n','-'*50)
        Soesc = soes()

print()
