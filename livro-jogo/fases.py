from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        nome = input("Insira seu nome: ")
        self.__descricao = f'''*** A aventura começa! ***
        Você é {nome}, uma pessoa comum que, em um evento inesperado, se vê no centro de um triângulo amoroso… 
        Duas opções de romance surgem na sua vida ao mesmo tempo, e cada escolha leva a novos dilemas e reviravoltas hilárias.
        Será que você encontra o amor verdadeiro ou acaba preso em um desastre romântico?
        
        Mensagem de Ana (uma pessoa divertida, espontânea e caótica) te convidando para um encontro surpresa.
        Mensagem de Sara (uma pessoa charmosa, inteligente e romântica) te chamando para um jantar elegante.'''
        self.__opcoes = ["Aceitar o convite de Ana", "Aceitar o convite de Sara"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return EncontroAna()
        elif escolha == 1:
            return EncontroSara()

# ----------------------- Ana ----------------------------

class EncontroAna(Fase):
    def __init__(self):
        self.__descricao = '''*** Encontro Selvagem com Ana ***
        Ana te leva para um encontro inesperado: um karaokê cheio de gente animada.
        Lá, você descobre que um ex de Ana ainda está por perto e claramente quer atrapalhar o encontro!'''
        self.__opcoes = ["Enfrentar o ex com confiança (macho alpha sigma redpill)", "Tentar sair discretamente com Sam (covarde)"]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return EnfrentarEx()
        elif escolha == 1:
            return SairDeFininho()

class EnfrentarEx(Fase):
    def __init__(self):
        self.__descricao = '''*** Confronto no Palco ***
        Você desafia o ex de Ana para um duelo de karaokê, e as coisas saem do controle!'''
        self.__opcoes = ["Dá um show incrível e impressiona Ana", "Faz uma apresentação desastrosa e acaba viralizando na internet"]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Show()
        elif escolha == 1:
            return Desastre()
        
class Show(Fase):
    def executar(self):
        print("\nFinal Feliz: Vocês têm uma noite incrível juntos e se apaixonam!")
        return None

class Desastre(Fase):
    def executar(self):
        print("\nFinal Triste: Você se torna famoso pelos motivos errados, e Ana some aos poucos da sua vida...")
        return None

class SairDeFininho(Fase):
    def __init__(self):
        self.__descricao = '''*** Fugindo do Problema ***
        Você tenta sair discretamente com Sam, mas o ex percebe e faz um escândalo!'''
        self.__opcoes = ["Corre com Sam para um táxi e parte para uma aventura noturna (se é que me entendes)", "Escorrega na pista molhada e cai de cara no chão"]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return Noite()
        elif escolha == 1:
            return Amizade()

class Noite(Fase):
    def executar(self):
        print("\nFinal Feliz: Vocês têm uma noite incrível juntos e se apaixonam!")
        return None
    
class Amizade(Fase):
    def executar(self):
        print("\nFinal Trágico: Sam ri tanto que começa a te ver mais como um(a) amigo(a)... O romance nunca acontece...")
        return None

# ----------------------- Sara ----------------------------

class EncontroSara(Fase):
    def __init__(self):
        self.__descricao = '''*** O Jantar Romântico com Sara ***
        Jamie te leva para um restaurante chique, mas você percebe que Jamie esqueceu a carteira em casa!'''
        self.__opcoes = ["Oferece pagar a conta como um gesto romântico", "Tenta sair do restaurante sem pagar "]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return PagarConta()
        elif escolha == 1:
            return SairDoRestaurante()

class PagarConta(Fase):
    def __init__(self):
        self.__descricao = '''*** A Noite da Generosidade ***
        A Noite da Generosidade
        Jamie fica impressionado(a) com seu gesto, mas sente que precisa retribuir.'''
        self.__opcoes = ["Aceita um segundo encontro, agora pago por Jamie", "Faz uma piada sobre nunca ser reembolsado e ofende Jamie chamando-a de interesseira"]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return SegundoEncontro()
        elif escolha == 1:
            return Ofender()

class SegundoEncontro(Fase):
    def executar(self):
        print("\nFinal Feliz: Vocês começam a namorar e têm vários encontros incríveis!)")
        return None
    
class Ofender(Fase):
    def executar(self):
        print("\nFinal Engraçado: Sara some e você nunca vê seu dinheiro de volta!)")
        return None

class SairDoRestaurante(Fase):
    def __init__(self):
        self.__descricao = '''*** O Plano de Fuga Maluco ***
        Vocês tentam escapar discretamente, mas são pegos pelo gerente do restaurante.'''
        self.__opcoes = ["Faz um discurso dramático e convence o gerente a perdoar vocês.", "São obrigados a lavar pratos juntos por horas."]

    def executar(self):
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)
        
        if escolha == 0:
            return DiscursoDramatico()
        elif escolha == 1:
            return LavaPrato()
        
class DiscursoDramatico(Fase):
    def executar(self):
        print("\nFinal Feliz: Jamie se apaixona ainda mais pela sua coragem e criatividade!")
        return None
    
class LavaPrato(Fase):
    def executar(self):
        print("\nFinal Engraçado: Vocês acabam discutindo tanto na cozinha que decidem que um romance não vai funcionar!")
        return None
        
class SairDoJogo(Fase):
    def executar(self):
        return None