import time

from forca.constantes import FORCAIMG
from forca.funcoes import gera_palavra_aleatoria
from forca.funcoes import imprime_jogo
from forca.funcoes import jogar_novamente
from forca.funcoes import le_palavras
from forca.funcoes import recebe_palpite
from forca.funcoes import verifica_se_ganhou


def main():
    """
    Função Principal do programa
    """

    letras_erradas = list()
    letras_acertadas = list()

    # lista as palavras disponíveis para o jogo
    palavras = le_palavras()

    # seleciona uma palavra aleatória
    palavra_secreta = gera_palavra_aleatoria(palavras).upper()

    # cria o loop do jogo
    jogando = True
    while jogando:
        # imprime o estado do jogo atual
        time.sleep(0.3)
        imprime_jogo(letras_erradas, letras_acertadas, palavra_secreta)
        time.sleep(0.3)

        # recebe um palpite do jogador
        palpite = recebe_palpite(letras_erradas + letras_acertadas)

        # adiciona o palpite ao dicionário adequado
        if palpite in palavra_secreta:
            letras_acertadas.append(palpite)
        else:
            letras_erradas.append(palpite)

        # verifica se o usuário ganhou o jogo
        if verifica_se_ganhou(palavra_secreta, letras_acertadas):
            time.sleep(0.3)
            print("Exato! A palavra secreta é " + palavra_secreta + "! Você ganhou!!")
            jogando = False

        # verifica se o usuário perdeu o jogo
        elif len(letras_erradas) == len(FORCAIMG) - 1:
            time.sleep(0.3)
            print("Você excedeu o seu limite de palpites!")
            print(
                "Depois de "
                + str(len(letras_erradas))
                + " letras erradas e "
                + str(len(letras_acertadas)),
                end=" ",
            )
            print("palpites corretos, a palavra era " + palavra_secreta + ".")

            jogando = False

        # se o usuário terminar o jogo
        if not jogando:
            # pede para jogar novamente
            time.sleep(0.3)
            if jogar_novamente():
                letras_erradas = list()
                letras_acertadas = list()
                jogando = True
                palavra_secreta = gera_palavra_aleatoria(palavras).upper()





main()