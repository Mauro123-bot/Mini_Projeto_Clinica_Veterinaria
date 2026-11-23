# Este arquivo roda os testes de cada módulo do projeto.

# Traz as classes No, ListaEncadeada e Fila do arquivo estruturas.py.
from estruturas import No, ListaEncadeada, Fila


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


# Função que testa a remoção na lista encadeada (Módulo 2, parte 2).
def teste_remocao():
    # Mostra o título do teste.
    print("Teste do Módulo 2: remoção na lista")
    # Cria uma lista vazia.
    lista = ListaEncadeada()
    # Insere quatro animais na lista.
    lista.inserir_fim("Rex")
    lista.inserir_fim("Mia")
    lista.inserir_fim("Thor")
    lista.inserir_fim("Luna")
    # Remove um item do meio (Mia) e mostra se deu certo (True).
    print("Removeu Mia?", lista.remover("Mia"))
    # Remove o primeiro item (Rex) e mostra se deu certo (True).
    print("Removeu Rex?", lista.remover("Rex"))
    # Remove o último item (Luna) e mostra se deu certo (True).
    print("Removeu Luna?", lista.remover("Luna"))
    # Tenta remover um item que não existe (deve mostrar False).
    print("Removeu Bob?", lista.remover("Bob"))
    # Mostra o que sobrou na lista (só Thor).
    lista.exibir()
    # Insere um novo item para conferir que a cauda continua correta.
    lista.inserir_fim("Nina")
    # Mostra a lista final (Thor e Nina).
    lista.exibir()
    # Mostra o tamanho final (deve ser 2).
    print("Tamanho:", lista.tamanho)


# Função que testa o Módulo 3 (fila).
def teste_modulo_3():
    # Mostra o título do teste.
    print("Teste do Módulo 3: fila")
    # Cria uma fila vazia.
    fila = Fila()
    # Espia a fila vazia: deve mostrar None, sem dar erro.
    print("Primeiro da fila vazia:", fila.espiar())
    # Tenta tirar alguém da fila vazia: deve mostrar None, sem dar erro.
    print("Saiu da fila vazia:", fila.desenfileirar())
    # Três animais chegam, nesta ordem.
    fila.enfileirar("Rex")
    fila.enfileirar("Mia")
    fila.enfileirar("Thor")
    # Mostra a fila inteira, do primeiro ao último.
    fila.exibir()
    # Espia o primeiro sem tirá-lo (deve ser Rex).
    print("Primeiro da fila:", fila.espiar())
    # Tira o primeiro: sai Rex, que chegou antes.
    print("Saiu:", fila.desenfileirar())
    # Tira o próximo: sai Mia.
    print("Saiu:", fila.desenfileirar())
    # Mostra quantos ainda esperam (deve ser 1).
    print("Tamanho:", fila.tamanho)
    # Tira o último: sai Thor.
    print("Saiu:", fila.desenfileirar())
    # Confere que a fila ficou vazia (deve mostrar True).
    print("Vazia?", fila.esta_vazia())
    # Um novo animal chega, para conferir que a fila funciona depois de esvaziar.
    fila.enfileirar("Luna")
    # Espia o primeiro (deve ser Luna).
    print("Primeiro da fila:", fila.espiar())


# Roda o teste do Módulo 1.
teste_modulo_1()
# Roda o teste do Módulo 2.
teste_modulo_2()
# Roda o teste de remoção.
teste_remocao()
# Roda o teste do Módulo 3.
teste_modulo_3()
