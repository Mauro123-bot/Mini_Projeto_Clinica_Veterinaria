# Este arquivo roda os testes de cada módulo do projeto.

# Traz as classes No e ListaEncadeada do arquivo estruturas.py.
from estruturas import No, ListaEncadeada


# Função que testa o Módulo 1 (classe No).
def teste_modulo_1():
    # Mostra o título do teste.
    print("Teste do Módulo 1: classe No")
    # Cria um nó com o dado "Rex".
    n1 = No("Rex")
    # Cria outro nó com o dado "Mia".
    n2 = No("Mia")
    # Liga o primeiro nó ao segundo pelo ponteiro.
    n1.proximo = n2
    # Mostra o dado do primeiro nó (Rex).
    print(n1.dado)
    # Vai do primeiro ao segundo nó pelo ponteiro e mostra o dado (Mia).
    print(n1.proximo.dado)
    # Mostra o ponteiro do segundo nó, que não aponta para ninguém (None).
    print(n2.proximo)


# Função que testa o Módulo 2 (lista encadeada).
def teste_modulo_2():
    # Mostra o título do teste.
    print("Teste do Módulo 2: lista encadeada")
    # Cria uma lista vazia.
    lista = ListaEncadeada()
    # Confere que a lista começa vazia (deve mostrar True).
    print("Vazia?", lista.esta_vazia())
    # Insere "Rex" no fim da lista.
    lista.inserir_fim("Rex")
    # Insere "Mia" no fim da lista.
    lista.inserir_fim("Mia")
    # Insere "Thor" no fim da lista.
    lista.inserir_fim("Thor")
    # Mostra todos os itens, na ordem em que foram inseridos.
    lista.exibir()
    # Mostra quantos itens a lista tem (deve ser 3).
    print("Tamanho:", lista.tamanho)
    # Confere que a lista não está mais vazia (deve mostrar False).
    print("Vazia?", lista.esta_vazia())


# Roda o teste do Módulo 1.
teste_modulo_1()
# Roda o teste do Módulo 2.
teste_modulo_2()