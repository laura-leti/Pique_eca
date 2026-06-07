nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))
tem_filhos = input("Você possui filhos? (S/N): ").upper()

while tem_filhos != "S" and tem_filhos != "N":
    print("Resposta inválida!")
    tem_filhos = input("Você possui filhos? (S/N): ").upper()
convive_criancas = "N"

if tem_filhos == "N":
    convive_criancas = input("Possui convivência com crianças? (S/N): ").upper()
    
    while convive_criancas != "S" and convive_criancas != "N":
        print("Resposta inválida!")
        convive_criancas = input("Possui convivência com crianças? (S/N): ").upper()
        