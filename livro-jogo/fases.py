from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao = '''A aventura começa!
        Você está em um laboratório misterioso e precisa escapar.
        Há uma porta de ferro trancada e um duto de ventilação ao lado.
        Qual caminho você escolhe?'''
        self.__opcoes = ["Tentar abrir a porta", "Entrar no duto"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return SalaControle()
        elif escolha == 1:
            return DutoVentilacao()

class SalaControle(Fase):
    def __init__(self):
        self.__descricao = '''Você encontra um painel de controle e vê uma câmera mostrando um guarda se aproximando.
        Há uma chave no painel. Você pode pegar a chave ou se esconder.'''
        self.__opcoes = ["Pegar a chave", "Se esconder"]

    def executar(self):
        print("\nSala de Controle")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return CorredorPrincipal()
        elif escolha == 1:
            return Capturado()

class DutoVentilacao(Fase):
    def __init__(self):
        self.__descricao = '''Você rasteja pelo duto e encontra uma saída para um depósito.
        Você pode continuar rastejando ou sair pelo alçapão.'''
        self.__opcoes = ["Continuar rastejando", "Sair pelo alçapão"]

    def executar(self):
        print("\nDuto de Ventilação")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return SalaServidor()
        elif escolha == 1:
            return Deposito()

class CorredorPrincipal(Fase):
    def executar(self):
        print("\nVocê usa a chave para abrir a porta principal e escapa! Parabéns!")
        return None

class Capturado(Fase):
    def executar(self):
        print("\nO guarda te encontra e você é capturado! Fim de jogo.")
        return None

class SalaServidor(Fase):
    def executar(self):
        print("\nVocê chega à sala do servidor e desativa os alarmes, facilitando sua fuga.")
        return CorredorPrincipal()

class Deposito(Fase):
    def executar(self):
        print("\nVocê entra no depósito e encontra um uniforme de funcionário. Disfarçado, você caminha para a saída.")
        return CorredorPrincipal()

class SairDoJogo(Fase):
    def executar(self):
        return None