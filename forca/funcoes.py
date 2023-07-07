import random
import typing

from .constantes import FORCAIMG


def le_palavras() -> typing.List[str]:
    """
    Le arquivo com palavras que podem ser utilizadas
    como parte do jogo
    """
    with open("palavras.txt") as f:
        return f.readlines()


def gera_palavra_aleatoria(palavras: str) -> typing.List[str]:
    """
    Função que retorna uma string a partir da
    lista de palavras

    :param palavras: lista com palavras que podem ser sorteadas
    :return: palavra secreta do jogo
    """
    return random.choice(palavras).replace("\n", "")


def imprime_com_espacos(palavra: typing.Union[str, typing.List[str]]) -> None:
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings

    :param palavra: palavra secreta do jogo
    """
    for letra in palavra:
        print(letra, end=" ")
    print()


def imprime_jogo(
    letras_erradas: typing.List[str],
    letras_acertadas: typing.List[str],
    palavra_secreta: str,
) -> None:
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta

    :param letras_erradas: lista de letras chutadas incorretamente
    :param letras_acertadas: lista de letras chutadas corretamente
    :param palavra_secreta: palavra secreta do jogo
    """
    print(FORCAIMG[len(letras_erradas)] + "\n")

    print("Letras Erradas:", end=" ")
    imprime_com_espacos(letras_erradas)

    vazio = "_" * len(palavra_secreta)
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] in letras_acertadas:
            vazio = vazio[:i] + palavra_secreta[i] + vazio[i + 1 :]

    imprime_com_espacos(vazio)


def recebe_palpite(palpites_feitos: typing.List[str]) -> str:
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado

    :param palpites_feitos: lista de letras chutadas anteriormente
    :return: nova letra chutada
    """
    while True:
        palpite = input("Advinhe uma letra.\n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in palpites_feitos:
            print("Você já chutou esta letra. Escolha novamente.")
        elif not "A" <= palpite <= "Z":
            print("Por favor escolha apenas letras.")
        else:
            return palpite


def jogar_novamente() -> bool:
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta

    :return: True se o jogador informou que deseja jogar novamente
    """
    return input("Você quer jogar novamente? (sim ou nao)\n").upper().startswith("S")


def verifica_se_ganhou(
    palavra_secreta: str, letras_acertadas: typing.List[str]
) -> bool:
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta

    :param palavra_secreta: palavra secreta do jogo
    :param letras_acertadas: lista de letras chutadas corretamente
    :return: booleano informando se o jogador ganhou o jogo
    """
    return set(list(palavra_secreta)) == set(letras_acertadas)