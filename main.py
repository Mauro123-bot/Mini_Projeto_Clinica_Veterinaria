# Este arquivo roda os testes de cada módulo do projeto.

# Traz as estruturas genéricas do arquivo estruturas.py.
from estruturas import No, ListaEncadeada, Fila, Pilha
# Traz as classes e funções da clínica do arquivo clinica.py.
from clinica import ControleAtendimento, CadastroTutores, criar_arvore_sistemas, Estoque
from clinica import Atendimento, ControleProntuarios, Caixa
# Traz o tipo de data do Python, para montar as datas dos lotes.
from datetime import date


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


# Função que testa o Módulo 7 (estoque: Lista de produtos + Fila de lotes).
def teste_modulo_7():
    # Mostra o título do teste.
    print("Teste do Módulo 7: estoque de medicamentos e vacinas")
    # Fixa a data de hoje do teste, para o resultado ser sempre o mesmo.
    hoje = date(2026, 11, 24)
    # Cria o estoque vazio.
    estoque = Estoque()
    # Cadastra três produtos, cada um com o seu mínimo e o seu destino de descarte.
    estoque.cadastrar_produto("AMX", "Amoxicilina 250 mg", 20,
                              "resíduo químico (grupo B), recolhido por empresa licenciada")
    estoque.cadastrar_produto("VAR", "Vacina antirrábica", 10,
                              "resíduo biológico (grupo A), tratamento antes do descarte")
    estoque.cadastrar_produto("SER", "Seringa com agulha", 50,
                              "perfurocortante (grupo E), caixa rígida própria")
    # Entram três lotes de amoxicilina, comprados em datas e preços diferentes.
    estoque.entrada_lote("AMX", "VetFarma", 1.50, 3.00, date(2026, 6, 1), date(2026, 11, 1), 10)
    estoque.entrada_lote("AMX", "VetFarma", 1.60, 3.20, date(2026, 8, 1), date(2027, 8, 1), 30)
    estoque.entrada_lote("AMX", "PetMed", 1.40, 3.00, date(2026, 10, 1), date(2027, 10, 1), 20)
    # Entra um lote de vacina que vence em breve.
    estoque.entrada_lote("VAR", "BioVet", 25.00, 60.00, date(2026, 9, 10), date(2026, 12, 10), 15)
    # Entra um lote de seringas.
    estoque.entrada_lote("SER", "MedSul", 0.50, 1.50, date(2026, 10, 15), date(2029, 10, 15), 100)
    # Mostra o estoque inicial.
    estoque.exibir()
    # Avisa os lotes que vencem nos próximos 30 dias (a vacina).
    estoque.alerta_vencimento_proximo(30, hoje)
    # Descarta os vencidos: o primeiro lote de amoxicilina venceu em 01/11.
    estoque.descartar_vencidos(hoje)
    # Retira 35 amoxicilinas: consome o lote de agosto (30) e 5 do lote de outubro.
    estoque.retirar("AMX", 35, hoje)
    # Tenta retirar mais do que existe: deve ser recusado.
    estoque.retirar("AMX", 100, hoje)
    # Ajuste de inventário: a contagem física achou só 8 vacinas.
    estoque.ajustar_quantidade("VAR", 8)
    # Mostra o estoque final.
    estoque.exibir()
    # Mostra as perdas registradas.
    print("Perdas registradas:")
    estoque.perdas.exibir()


# Função que testa o Módulo 8 (pilha e prontuário).
def teste_modulo_8():
    # Mostra o título do teste da pilha.
    print("Teste do Módulo 8: pilha")
    # Cria uma pilha vazia.
    pilha = Pilha()
    # Empilha três itens.
    pilha.empilhar("consulta")
    pilha.empilhar("exame")
    pilha.empilhar("curativo")
    # O topo é o último que entrou (curativo).
    print("Topo:", pilha.espiar())
    # Desempilha: sai primeiro o curativo, depois o exame (LIFO).
    print("Saiu:", pilha.desempilhar())
    print("Saiu:", pilha.desempilhar())
    # Mostra o tamanho restante (1).
    print("Tamanho:", pilha.tamanho)

    # Mostra o título do teste do prontuário.
    print("Teste do Módulo 8: prontuário")
    # Cria o controle de prontuários.
    controle = ControleProntuarios()
    # Simula o animal que foi chamado ao consultório.
    atendimento = Atendimento("Rex", "Ana", "vômito")
    # Abre o prontuário com a veterinária responsável.
    prontuario = controle.abrir(atendimento, "Dra. Paula")
    # Faz o diagnóstico na árvore e copia os achados para o prontuário.
    arvore = criar_arvore_sistemas()
    arvore.marcar_alterado("Estômago")
    prontuario.registrar_achados(arvore)
    # Ao longo do atendimento, entram medicamentos e procedimentos.
    prontuario.adicionar_procedimento("Consulta", 150.00)
    prontuario.adicionar_medicamento("AMX", "Amoxicilina 250 mg", 10)
    prontuario.adicionar_procedimento("Exame de sangue", 120.00)
    prontuario.adicionar_medicamento("SER", "Seringa com agulha", 2)
    prontuario.adicionar_procedimento("Ultrassom", 200.00)
    # O tutor não autoriza o exame de sangue: removido do meio da lista.
    prontuario.remover_procedimento("Exame de sangue")
    # A última inclusão (ultrassom) é desfeita com a pilha.
    prontuario.desfazer_ultima_inclusao()
    # Tenta fechar antes da alta: deve ser recusado.
    controle.fechar(prontuario.numero)
    # O animal recebe alta.
    prontuario.dar_alta()
    # Agora o prontuário pode ser fechado.
    controle.fechar(prontuario.numero)
    # Depois de fechado, não aceita mais inclusões.
    prontuario.adicionar_procedimento("Banho", 60.00)
    # Mostra o prontuário final.
    prontuario.exibir()


# Função que testa os Módulos 9 e 10 (pagamento, baixa no estoque e consumo).
def teste_modulos_9_e_10():
    # Mostra o título do teste.
    print("Teste dos Módulos 9 e 10: pagamento, baixa no estoque e consumo")
    # Fixa a data de hoje do teste.
    hoje = date(2026, 11, 24)
    # Monta um estoque pequeno.
    estoque = Estoque()
    estoque.cadastrar_produto("AMX", "Amoxicilina 250 mg", 20,
                              "resíduo químico (grupo B), recolhido por empresa licenciada")
    estoque.cadastrar_produto("SER", "Seringa com agulha", 50,
                              "perfurocortante (grupo E), caixa rígida própria")
    estoque.entrada_lote("AMX", "VetFarma", 1.60, 3.20, date(2026, 8, 1), date(2027, 8, 1), 30)
    estoque.entrada_lote("AMX", "PetMed", 1.40, 3.00, date(2026, 10, 1), date(2027, 10, 1), 20)
    estoque.entrada_lote("SER", "MedSul", 0.50, 1.50, date(2026, 10, 15), date(2029, 10, 15), 100)
    # Cria o controle de prontuários e o caixa, que trabalha com os dois.
    controle = ControleProntuarios()
    caixa = Caixa(estoque, controle)
    # Abre o prontuário do Rex e inclui medicamentos e procedimento.
    p1 = controle.abrir(Atendimento("Rex", "Ana", "vômito"), "Dra. Paula")
    p1.adicionar_medicamento("AMX", "Amoxicilina 250 mg", 10)
    p1.adicionar_medicamento("SER", "Seringa com agulha", 2)
    p1.adicionar_procedimento("Consulta", 150.00)
    # Tenta pagar antes da alta: deve ser recusado.
    caixa.fechar_e_pagar(p1.numero, "Ana", "cartão", 3, hoje)
    # O Rex recebe alta e Ana paga no cartão em 3 vezes.
    p1.dar_alta()
    caixa.fechar_e_pagar(p1.numero, "Ana", "cartão", 3, hoje)
    # Abre o prontuário da Mia, pedindo mais amoxicilina do que existe.
    p2 = controle.abrir(Atendimento("Mia", "Carlos", "falta de apetite"), "Dr. João")
    p2.adicionar_medicamento("SER", "Seringa com agulha", 1)
    p2.adicionar_medicamento("AMX", "Amoxicilina 250 mg", 100)
    p2.dar_alta()
    # O fechamento é recusado e NADA é baixado, nem a seringa.
    caixa.fechar_e_pagar(p2.numero, "Carlos", "PIX", data_referencia=hoje)
    # O tutor não autoriza a amoxicilina extra; ela sai e o fechamento é feito via PIX.
    p2.remover_medicamento("AMX")
    p2.adicionar_procedimento("Consulta", 150.00)
    caixa.fechar_e_pagar(p2.numero, "Carlos", "PIX", data_referencia=hoje)
    # Mostra o estoque depois das baixas.
    estoque.exibir()
    # Mostra o consumo de cada animal.
    caixa.consumo_por_animal("Ana", "Rex")
    caixa.consumo_por_animal("Carlos", "Mia")
    # Mostra o total recebido no caixa.
    print(f"Total recebido no caixa: R$ {caixa.total_recebido():.2f}")


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
# Roda o teste do Módulo 7.
teste_modulo_7()
# Roda o teste do Módulo 8.
teste_modulo_8()
# Roda o teste dos Módulos 9 e 10.
teste_modulos_9_e_10()
