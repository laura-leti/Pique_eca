"""
Módulo: Canais de Disque Denúncia
Projeto: MINI-GAME — Maio Laranja (Pique ECA)
Responsável: [Jeniffer Thalya Ferreira do Nascimento]
"""

def get_canais_de_denuncia():
    canais = [
        {
            "nome": "Disque 100",
            "numero": "0800 55 0140",
            "funcao": "Denúncia anônima de abuso sexual, maus-tratos e exploração",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Polícia Militar",
            "numero": "190",
            "funcao": "Emergência policial",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Conselho Tutelar",
            "numero": "Consulte sua cidade",
            "funcao": "Proteção e orientação à criança",
            "disponibilidade": "Horário comercial"
        },
        {
            "nome": "Ligue 180",
            "numero": "180",
            "funcao": "Atendimento à mulher e a criança",
            "disponibilidade": "24h, todos os dias"
        },
        {
            "nome": "Samu",
            "numero":"192",
            "funcao":"Emergência médica",
            "disponibilidade":"24h, todos os dias"
        }
    ]
    return canais


def mostrar_menu_denuncia():
    canais = get_canais_de_denuncia()
    
    print("\n" + "=" * 50)
    print("🛑 CANAIS OFICIAIS DE DENÚNCIA 🛑")
    print("=" * 50)
    print("Anote os canais abaixo:\n")
    
    for i, canal in enumerate(canais, 1):
        print(f"{i}. {canal['nome']} ")
        print(f"📞 Contato: {canal['numero']}")
        print(f"📝 Função: {canal['funcao']}")
        print(f"⏰ Disponibilidade: {canal['disponibilidade']}\n")
    
    print("=" * 50)
    input("Pressione ENTER para continuar!")


if __name__ == "__main__":
    mostrar_menu_denuncia()