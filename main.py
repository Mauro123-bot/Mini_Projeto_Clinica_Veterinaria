from estruturas import No


def teste_modulo_1():
    print("Teste do Módulo 1: classe No")
    n1 = No("Rex")
    n2 = No("Mia")
    n1.proximo = n2
    print(n1.dado)
    print(n1.proximo.dado)
    print(n2.proximo)


teste_modulo_1()