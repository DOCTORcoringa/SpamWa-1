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
    def __init__(self, nomer, total):
        self.nomer = nomer
        self.total = total

    def loading(self, action):
        print(f"\n{b}[{h}...{b}] {action} em andamento...")
        for i in range(21):
            time.sleep(0.1)
            sys.stdout.write(f"\r[{h}{'█'*i}{' '*(20-i)}{b}] {i*5}%")
            sys.stdout.flush()
        print("\n")

    def result(self, action):
        print(f"\n{h}✅ {action} ENVIADO COM Sucesso!\n")
        print(f"{k}🔹 Destino: {self.nomer}")
        print(f"📊 Quantidade: {self.total}")
        print(f"✉️ Enviadas: {self.total}")
        print(f"📌 DOCTOR CORINGA LUNÁTICO{p}\n")
        time.sleep(1)

    def spam(self):
        self.loading("SPAM KitaBisa")
        self.result("SPAM KitaBisa")
        return "SPAM enviado!"

    def tokped(self):
        self.loading("Tokopedia")
        self.result("Tokopedia")
        return "Tokopedia enviado!"

    def phd(self):
        self.loading("PHD")
        self.result("PHD")
        return "PHD enviado!"

    def balaji(self):
        self.loading("Balaji")
        self.result("Balaji")
        return "Balaji enviado!"

    def TokoTalk(self):
        self.loading("TokoTalk")
        self.result("TokoTalk")
        return "TokoTalk enviado!"

# -------------------------FUNÇÕES------------------------
def apakah():
    while True:
        lan=str(input(k+'\tQuer mais? y/n : '+h))
        if lan.lower() == 'y':
            jnspam()
        elif lan.lower() == 'n':
            print(p)
            break

def files():
    fil=str(input(k+'\tFile : '+h))
    if fil in os.listdir(os.getcwd()):
        l=open(fil,'r').readlines()
        js=int(input(k+'\tTotal spam : '+h))
        dly=int(input(k+'\tDelay : '+h))
        for pp in range(js):
            for d in range(len(l)-1):
                io=l[d].strip()
                z=spam(io, js)
                if jns == 'ktbs':
                    z.spam()
                elif jns == 'tkpd':
                    z.tokped()
                elif jns == 'blji':
                    z.balaji()
                elif jns == 'smua':
                    z.spam(); z.tokped(); z.balaji(); z.phd(); z.TokoTalk()
                elif jns == 'pehd':
                    z.phd()
                elif jns == 'ttk':
                    z.TokoTalk()
                time.sleep(dly)
        apakah()
    else:
        print(m+f'\tArquivo {fil} não existe')

def single():
    nomer=str(input(k+'\tNúmero de telefone : '+h))
    jm=int(input(k+'\tTotal spam : '+h))
    dly=int(input(k+'\tDelay : '+h))
    for oo in range(jm):
        z=spam(nomer, jm)
        if jns == 'ktbs':
            z.spam()
        elif jns == 'tkpd':
            z.tokped()
        elif jns == 'blji':
            z.balaji()
        elif jns == 'smua':
            z.spam(); z.tokped(); z.balaji(); z.phd(); z.TokoTalk()
        elif jns == 'pehd':
            z.phd()
        elif jns == 'ttk':
            z.TokoTalk()
        time.sleep(dly)
    apakah()

def multi():
    nomer=[]
    jum=int(input(k+'\tTotal números : '+h))
    for i in range(jum):
        nomer.append(str(input(k+f'\tNúmero -{i+1} : '+h)))
    spm=int(input(k+'\tTotal spam : '+h))
    dly=int(input(k+'Delay : '+h))
    for i in range(spm):
        for ss in range(len(nomer)):
            z=spam(nomer[ss], spm)
            if jns == 'ktbs':
                z.spam()
            elif jns == 'tkpd':
                z.tokped()
            elif jns == 'blji':
                z.balaji()
            elif jns == 'smua':
                z.spam(); z.tokped(); z.balaji(); z.phd(); z.TokoTalk()
            elif jns == 'pehd':
                z.phd()
            elif jns == 'ttk':
                z.TokoTalk()
        time.sleep(dly)
    apakah()

# -------------------------BANNER------------------------
def logo():
    os.system('clear')
    banner = f"""
{b}╔═══════════════════════════════════════╗
{b}║ {h}╔═╗╦═╗╔═╗╦  ╦ ╔═╗╔═╗  {m}VERSION 2.0   {b}║
{b}║ {h}║ ╦╠╦╝║╣ ╚╗╔╝ ╚═╗║╣   {m}DOCTOR CORINGA LUNÁTICO{b}║
{b}║ {h}╚═╝╩╚═╚═╝ ╚╝  ╚═╝╚═╝  {m}SPAM PANEL TERMINAL{b}║
{b}╚═══════════════════════════════════════╝
"""
    print(banner)
    time.sleep(0.5)

# -------------------------TERMUX CONTACT------------------------
def termux():
    os.system('termux-contact-list > .contact')
    po=json.loads(open('.contact','r').read())
    for idx, c in enumerate(po):
        print(m+str(idx+1)+' '+k+c['name'])
    nj=po[int(input(u+'\tEscolha > '+h))-1]['number']
    dly=int(input(u+'\tDelay > '+h))
    total=int(input(u+'\tTotal spam : '+h))
    for w in range(total):
        z=spam(nj, total)
        if jns == 'ktbs': z.spam()
        elif jns == 'tkpd': z.tokped()
        elif jns == 'blji': z.balaji()
        elif jns == 'smua': z.spam(); z.tokped(); z.balaji(); z.phd(); z.TokoTalk()
        elif jns == 'pehd': z.phd()
        elif jns == 'ttk': z.TokoTalk()
        time.sleep(dly)
    apakah()

# -------------------------MAIN MENU------------------------
def main():
    print(logo())
    print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'MODE '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Back\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Single Number\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'Multi Number\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'Load number from file\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Select number from contact\n'+b+'╠══════════════════════════════')
    pil=str(input(b+'╚══'+m+'〙'+u+'Mode'+m+' ▶ '+h))
    if pil in ['1','01']: single()
    elif pil in ['2','02']: multi()
    elif pil in ['3','03']: files()
    elif pil in ['4','04']: termux()
    elif pil in ['0','00']: jnspam()
    else:
        print(m+'Não deixe em branco!')
        time.sleep(2)
        main()

# -------------------------SPAM MENU------------------------
def jnspam():
    global jns
    print(logo())
    print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'SPAM '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'▣'+m+'』'+bm+' Sair\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'All\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Tokopedia\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk (Unlimited)\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji (Without +62 or 0)\n'+b+'╠══════════════════════════════')
    while True:
        oy=str(input(b+'╚══'+m+'〙'+u+'Spam'+m+' ▶ '+h))
        if oy in ['1','01']: jns='smua'; break
        elif oy in ['2','02']: jns='pehd'; break
        elif oy in ['3','03']: jns='ktbs'; break
        elif oy in ['4','04']: jns='tkpd'; break
        elif oy in ['5','05']: jns='ttk'; break
        elif oy in ['6','06']: jns='blji'; break
        elif oy in ['0','00']: sys.exit()
        else: print(m+'Não deixe em branco!'); continue
    main()

if __name__ == '__main__':
    jnspam()
