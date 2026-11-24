# Este arquivo roda os testes de cada módulo do projeto.

# Traz as classes No, ListaEncadeada e Fila do arquivo estruturas.py.
from estruturas import No, ListaEncadeada, Fila
# Traz as classes e funções da clínica do arquivo clinica.py.
from clinica import ControleAtendimento, CadastroTutores, criar_arvore_sistemas


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


# Função que testa o Módulo 4 (atendimento com Fila + Fila).
def teste_modulo_4():
    # Mostra o título do teste.
    print("Teste do Módulo 4: controle de atendimento")
    # Cria uma clínica com 2 consultórios.
    clinica = ControleAtendimento(2)
    # Chegam três casos normais, nesta ordem.
    clinica.registrar_chegada("Rex", "Ana", "vômito")
    clinica.registrar_chegada("Mia", "Carlos", "falta de apetite")
    clinica.registrar_chegada("Thor", "Beatriz", "ferimento na pata")
    # Depois chegam duas emergências.
    clinica.registrar_chegada("Bob", "Daniel", "atropelamento", emergencia=True)
    clinica.registrar_chegada("Luna", "Eva", "intoxicação", emergencia=True)
    # Mostra quem é o próximo: deve ser Bob, a primeira emergência.
    print("Próximo da vez:", clinica.proximo_da_vez().nome_animal)
    # Chama dois animais: devem ser Bob e Luna, as emergências, na ordem de chegada.
    clinica.chamar_proximo()
    clinica.chamar_proximo()
    # Tenta chamar um terceiro: os 2 consultórios estão ocupados.
    clinica.chamar_proximo()
    # Bob é liberado: o sistema chama automaticamente Rex, o primeiro da fila normal.
    clinica.liberar_consultorio("Bob")
    # Mostra a situação final das filas e dos consultórios.
    clinica.exibir_situacao()


# Função que testa o Módulo 5 (tutores e animais, Lista + Lista).
def teste_modulo_5():
    # Mostra o título do teste.
    print("Teste do Módulo 5: tutores e animais")
    # Cria o cadastro vazio.
    cadastro = CadastroTutores()
    # Cadastra dois tutores.
    cadastro.cadastrar_tutor("Ana", "111.111.111-11", "(19) 99999-1111")
    cadastro.cadastrar_tutor("Carlos", "222.222.222-22", "(19) 99999-2222")
    # Tenta cadastrar de novo o mesmo CPF: deve ser recusado.
    cadastro.cadastrar_tutor("Ana Maria", "111.111.111-11", "(19) 98888-0000")
    # Ana cadastra dois animais.
    cadastro.cadastrar_animal("111.111.111-11", "Rex", "cão", "labrador", 5)
    cadastro.cadastrar_animal("111.111.111-11", "Mia", "gato", "siamês", 3)
    # Carlos cadastra um animal.
    cadastro.cadastrar_animal("222.222.222-22", "Thor", "cão", "vira-lata", 8)
    # Tempo depois, Ana traz um terceiro animal: não há limite.
    cadastro.cadastrar_animal("111.111.111-11", "Nina", "coelho", "mini lop", 1)
    # Mostra o cadastro completo.
    cadastro.exibir()
    # Busca o tutor pelo CPF.
    print("Busca por CPF:", cadastro.buscar_por_cpf("222.222.222-22"))
    # Busca um animal pelo nome junto com o CPF do tutor (deve achar Mia).
    print("Busca Mia da Ana:", cadastro.buscar_animal("111.111.111-11", "Mia"))
    # Busca Thor com o CPF da Ana: Thor é do Carlos, então não deve achar (None).
    print("Busca Thor da Ana:", cadastro.buscar_animal("111.111.111-11", "Thor"))
    # Remove a Mia da lista da Ana.
    cadastro.remover_animal("111.111.111-11", "Mia")
    # Remove o tutor Carlos (e o Thor sai junto).
    cadastro.remover_tutor("222.222.222-22")
    # Mostra o cadastro final.
    cadastro.exibir()


# Função que testa o Módulo 6 (árvore de sistemas do animal).
def teste_modulo_6():
    # Mostra o título do teste.
    print("Teste do Módulo 6: árvore de sistemas do animal")
    # Monta a árvore pré-definida.
    arvore = criar_arvore_sistemas()
    # Exibe a árvore indentada, com tudo Saudável.
    arvore.exibir()
    # O veterinário marca o estômago como alterado, pelo nome.
    arvore.marcar_alterado("Estômago")
    # Marca a gengiva como alterada, pelo código.
    arvore.marcar_alterado("DG02")
    # Tenta marcar um item que não existe na árvore.
    arvore.marcar_alterado("Fígado")
    # Exibe a árvore de novo, já com os itens alterados.
    arvore.exibir()
    # Mostra a lista dos itens alterados, que irá para o prontuário.
    print("Itens alterados:")
    arvore.itens_alterados().exibir()


# Roda o teste do Módulo 1.
teste_modulo_1()
# Roda o teste do Módulo 2.
teste_modulo_2()
# Roda o teste de remoção.
teste_remocao()
# Roda o teste do Módulo 3.
teste_modulo_3()
# Roda o teste do Módulo 4.
teste_modulo_4()
# Roda o teste do Módulo 5.
teste_modulo_5()
# Roda o teste do Módulo 6.
teste_modulo_6()
