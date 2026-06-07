#MENU DE INICIALIZAÇÃO: 
import time
def linhas():
    print("=" *50)

linhas()
print('🧡 GUARDIÕES DA INFÂNCIA - MAIO LARANJA 🧡'.center(50))
linhas()
print(f"Seja bem-vindo(a)! Sua missão é ajudar na conscientização!" .upper())
time.sleep (2.0)

linhas()
print('CENTRAL DOS GUARDIÕES:'.center(50))
linhas()

print("1 - Orientações e prevenção")
print("2 - Canal de denúncia")
print("3 - Mini-game")
print("4 - Informações sobre a campanha")
print("5 - Encerrar missão")

opcao = int(input("\nEscolha uma opção: "))
