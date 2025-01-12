from random import randint as r
from time import sleep as s

palavras = ["SAGAZ", "AMAGO", "NEGRO", "TERMO", "EXITO", "MEXER", "NOBRE", "SENSO", "AFETO", "ALGOZ", "ETICA",
            "PLENA", "FAZER", "TENUE", "MUTUA", "ASSIM", "VIGOR", "SUTIL", "AQUEM", "POREM", "SECAO", "FOSSE",
            "PODER", "SANAR", "AUDAZ", "IDEIA", "CERNE", "INATO", "MORAL", "DESDE", "MUITO", "JUSTO", "QUIÇA",
            "HONRA", "TORPE", "SONHO", "RAZAO", "FUTIL", "ETNIA", "ICONE", "AMIGO", "ANEXO", "EGIDE", "TANGE",
            "LAPSO", "HAVER", "EXPOR", "DENGO", "TEMPO", "ENTAO"]
opc = "S"


def hud(msg="\033[32mTERMO\033[m EM \033[33mPYTHON\033[m"):
    men = msg
    print("\033[34m=\033[m"*51)
    print(f"{men:^65}")
    print(f"\033[34m=\033[m"*51)


while True:
    tentativa = 6
    hud()
    s(1)
    if opc == "N":
        s(1)
        break
    numero = r(0, len(palavras)-1)
    print("Tente uma palavra de \033[32m5\033[m letra:\n   _____")
    while True:
        if tentativa == 0:
            print("\033[31mForam todas as tentativas\033[m")
            s(2)
            opc = str(input("\nJogar de novo? \033[33m[S/N]\033[m:\n>> ")).upper().strip()
            print("\n"*100)
            break
        word = str(input("\033[36m>>\033[m ")).strip().upper()
        if len(word) != 5:
            print("\033[31mPalavra de tamanho inválido!\033[m")
            s(1)
        elif palavras[numero] == word:
            print("\033[32m\nJÁ GANHOU TAN TAN TAN!!\033[m")
            s(2)
            opc = str(input("\nJogar de novo? \033[33m[S/N]\033[m:\n>> ")).upper().strip()
            s(1)
            print("\n"*100)
            break
        else:
            palavra = palavras[numero]
            for c in range(0, 5):
                if palavra[c] == word[c]:
                    print(f"\033[32m{word[c]}\033[m", end=' ')
                elif word[c] in palavra:
                    print(f"\033[33m{word[c]}\033[m", end=' ')
                else:
                    print(f"\033[37m{word[c]}\033[m", end=' ')
        print()
        tentativa -= 1
print("Obrigado por jogar!")
print("Feito por: \033[36mRX4N\033[m")
s(4)
