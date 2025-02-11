class JogoUtil: 
    @staticmethod
    def exibir_opcoes(opcoes):
        for i, opcao in enumerate(opcoes, 1):
            print(f'{i}. {opcao}')
        print(f'{len(opcoes) + 1}. Sair')

    @staticmethod
    def fazer_escolha(opcoes):
        from fases import SairDoJogo
        while True:
            try:
                escolha = int(input("\nEscolha uma opção: ")) - 1
                if 0 <= escolha < len(opcoes):
                    return escolha
                elif escolha == len(opcoes):
                    print("\nVocê decidiu sair do game")
                    return SairDoJogo()
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Escolha inválida. Tente novamente.")
