#!/usr/bin/python
import time, sys, os

# -----------------------CORES----------------------------
p = '\x1b[0m'
h = '\x1b[92m'
m = '\x1b[91m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'

# ---------------------------Banner SPAM-----------------------
def banner():
    os.system("clear")
    print(f"""
{b}███████╗██████╗  ███╗   ███╗{h}██████╗ █████╗ ███╗   ███╗
{b}██╔════╝██╔══██╗████╗ ████║{h}██╔══██╗██╔══██╗████╗ ████║
{b}█████╗  ██████╔╝██╔████╔██║{h}██████╔╝███████║██╔████╔██║
{b}██╔══╝  ██╔═══╝ ██║╚██╔╝██║{h}██╔═══╝ ██╔══██║██║╚██╔╝██║
{b}███████╗██║     ██║ ╚═╝ ██║{h}██║     ██║  ██║██║ ╚═╝ ██║
{b}╚══════╝╚═╝     ╚═╝     ╚═╝{h}╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
{u}     "DCL PANEL - Controle total do seu SPAM"{p}
{h}     Criador: DOCTOR CORINGA LUNÁTICO
{h}     Versão: 2.0 | BY-2025
""")

# -------------------Função de barra de carregamento animada-----------
def carregamento(msg="Enviando"):
    print(f"\n{b}{msg}{p}")
    barra = 30
    for i in range(barra + 1):
        porcentagem = int((i / barra) * 100)
        print(f"\r{h}[{'■'*i}{' '*(barra-i)}] {porcentagem}%{p}", end="", flush=True)
        time.sleep(0.05)
    print("\n")

# -------------------Função para mostrar resultado final em caixa-----------
def resultado_final(destinos, quantidade, criador="DOCTOR CORINGA LUNÁTICO"):
    if type(destinos) != list:
        destinos = [destinos]
    conteudo = [
        f"✅ ENVIO REALIZADO COM SUCESSO!",
        f"🔹 Destinatário(s): {', '.join(destinos)}",
        f"📊 Quantidade: {quantidade}",
        f"📌 Criador: {criador}"
    ]
    largura = max(len(l) for l in conteudo) + 4
    print(f"\n{h}╔{'═'*largura}╗")
    for linha in conteudo:
        print(f"║ {linha.ljust(largura-2)} ║")
    print(f"╚{'═'*largura}╝\n")

# ---------------------------Função de envio com contador em tempo real---------------------------
def enviar(destinos, quantidade):
    if type(destinos) != list:
        destinos = [destinos]
    total = len(destinos) * quantidade
    contador = 0
    for dest in destinos:
        for i in range(quantidade):
            contador += 1
            print(f"\r{h}Enviando para {dest}... ({contador}/{total}){p}", end="", flush=True)
            time.sleep(0.2)
    print("\n")
    resultado_final(destinos, quantidade)

# ---------------------------Menu Principal-----------------------
def menu():
    while True:
        banner()
        print(b+'╔═══════════════════')
        print(b+'║'+h+'〘 MENU PRINCIPAL 〙')
        print(b+'╠═══════════════════'+b)
        print(b+'║'+m+'1'+h+') Spam Normal')
        print(b+'║'+m+'2'+h+') Spam Duplo')
        print(b+'║'+m+'3'+h+') Spam WhatsApp')
        print(b+'║'+m+'4'+h+') Denúncia')
        print(b+'║'+m+'0'+h+') Sair')
        escolha = input(b+'Escolha a opção ▶ '+h)
        
        if escolha == '1':
            numero = input(k+'Digite o número do destinatário: '+h)
            quantidade = int(input(k+'Quantidade: '+h))
            carregamento("Preparando envio...")
            enviar(numero, quantidade)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '2':
            numero1 = input(k+'Digite o primeiro número: '+h)
            numero2 = input(k+'Digite o segundo número: '+h)
            quantidade = int(input(k+'Quantidade: '+h))
            carregamento("Preparando envio...")
            enviar([numero1, numero2], quantidade)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '3':
            numero = input(k+'Digite o número do destinatário: '+h)
            quantidade = int(input(k+'Quantidade: '+h))
            carregamento("Preparando envio...")
            enviar(numero, quantidade)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '4':
            numero = input(k+'Digite o número para denúncia: '+h)
            quantidade = int(input(k+'Quantidade: '+h))
            carregamento("Preparando envio...")
            enviar(numero, quantidade)
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '0':
            sys.exit()
        else:
            print(m+'Opção inválida! Tente novamente.')
            time.sleep(1)

if __name__ == "__main__":
    menu()
