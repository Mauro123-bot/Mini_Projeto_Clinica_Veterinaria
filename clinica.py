# Este arquivo guarda as regras da Clínica Veterinária.
# Ele usa as estruturas genéricas do arquivo estruturas.py, mas não as modifica.

# Traz a lista encadeada, a fila e o nó de árvore criados no estruturas.py.
from estruturas import ListaEncadeada, Fila, NoArvore
# Traz a biblioteca de datas do Python, usada só para registrar datas e horas.
from datetime import datetime, date, timedelta


# ==================== MÓDULO 4: CONTROLE DE ATENDIMENTO ====================

# Cria a classe Atendimento: os dados de um animal que chegou à clínica.
class Atendimento:
    # Construtor: recebe os dados da chegada do animal.
    def __init__(self, nome_animal, nome_tutor, queixa, emergencia=False):
        # Guarda o nome do animal.
        self.nome_animal = nome_animal
        # Guarda o nome do tutor.
        self.nome_tutor = nome_tutor
        # Guarda a queixa relatada (ex.: vômito, ferimento na pata).
        self.queixa = queixa
        # Guarda se é um caso de emergência (True) ou normal (False).
        self.emergencia = emergencia
        # Registra automaticamente a data e a hora da chegada.
        self.chegada = datetime.now()

    # Define como o atendimento aparece quando é mostrado com print.
    def __str__(self):
        # Escolhe o texto do tipo de atendimento.
        tipo = "EMERGÊNCIA" if self.emergencia else "normal"
        # Formata a hora da chegada como horas:minutos:segundos.
        hora = self.chegada.strftime("%H:%M:%S")
        # Monta a frase com todos os dados do atendimento.
        return f"{self.nome_animal} (tutor: {self.nome_tutor}) - {self.queixa} - {tipo} - chegou às {hora}"


# Cria a classe ControleAtendimento: a espera e os consultórios da clínica.
class ControleAtendimento:
    # Construtor: recebe quantos consultórios a clínica tem.
    def __init__(self, total_consultorios):
        # Guarda o número total de consultórios.
        self.total_consultorios = total_consultorios
        # Cria a fila de emergências (atropelamento, intoxicação etc.).
        self.fila_emergencia = Fila()
        # Cria a fila de atendimento normal, por ordem de chegada.
        self.fila_normal = Fila()
        # Cria a lista dos animais que estão sendo atendidos agora.
        self.em_atendimento = ListaEncadeada()

    # Método que informa quantos consultórios estão livres.
    def consultorios_livres(self):
        # Livres = total de consultórios menos os ocupados.
        return self.total_consultorios - self.em_atendimento.tamanho

    # Método que registra a chegada de um animal e o coloca na fila certa.
    def registrar_chegada(self, nome_animal, nome_tutor, queixa, emergencia=False):
        # Cria o atendimento com os dados recebidos.
        atendimento = Atendimento(nome_animal, nome_tutor, queixa, emergencia)
        # Se for emergência...
        if emergencia:
            # ...entra no fim da fila de emergência.
            self.fila_emergencia.enfileirar(atendimento)
        # Se não for emergência...
        else:
            # ...entra no fim da fila normal.
            self.fila_normal.enfileirar(atendimento)
        # Mostra na tela que a chegada foi registrada.
        print(f"Chegada registrada: {atendimento}")

    # Método que mostra quem é o próximo a ser atendido, sem tirá-lo da fila.
    def proximo_da_vez(self):
        # Se houver alguém na fila de emergência...
        if not self.fila_emergencia.esta_vazia():
            # ...o próximo é o primeiro da emergência.
            return self.fila_emergencia.espiar()
        # Se não houver emergência, o próximo é o primeiro da fila normal.
        return self.fila_normal.espiar()

    # Método que chama o próximo animal para um consultório livre.
    def chamar_proximo(self):
        # Se não houver consultório livre, ninguém pode ser chamado.
        if self.consultorios_livres() == 0:
            # Avisa que todos os consultórios estão ocupados.
            print("Todos os consultórios estão ocupados. Aguarde.")
            # Devolve None, pois ninguém foi chamado.
            return None
        # Primeiro tenta tirar alguém da fila de emergência.
        if not self.fila_emergencia.esta_vazia():
            # Tira o primeiro da emergência.
            atendimento = self.fila_emergencia.desenfileirar()
        # Se a emergência estiver vazia, tenta a fila normal.
        elif not self.fila_normal.esta_vazia():
            # Tira o primeiro da fila normal.
            atendimento = self.fila_normal.desenfileirar()
        # Se as duas filas estiverem vazias...
        else:
            # ...avisa que não há ninguém esperando.
            print("Não há animais aguardando.")
            # Devolve None, pois ninguém foi chamado.
            return None
        # Coloca o animal chamado na lista de quem está em atendimento.
        self.em_atendimento.inserir_fim(atendimento)
        # Mostra na tela quem foi chamado.
        print(f"Chamado para o consultório: {atendimento.nome_animal}")
        # Devolve o atendimento chamado.
        return atendimento

    # Método que libera o consultório de um animal e chama o próximo automaticamente.
    def liberar_consultorio(self, nome_animal):
        # Começa a procurar o animal pelo primeiro da lista de atendimento.
        atual = self.em_atendimento.cabeca
        # Percorre a lista enquanto houver nós.
        while atual is not None:
            # Verifica se este é o animal procurado.
            if atual.dado.nome_animal == nome_animal:
                # Remove o atendimento da lista, liberando o consultório.
                self.em_atendimento.remover(atual.dado)
                # Mostra na tela que o consultório foi liberado.
                print(f"Consultório liberado por {nome_animal}.")
                # Chama automaticamente o próximo da espera.
                return self.chamar_proximo()
            # Avança para o próximo nó da lista.
            atual = atual.proximo
        # Se não encontrou o animal, avisa.
        print(f"{nome_animal} não está em atendimento.")
        # Devolve None, pois nada foi liberado.
        return None

    # Método que mostra a situação atual das filas e dos consultórios.
    def exibir_situacao(self):
        # Mostra a fila de emergência.
        print("Fila de emergência:")
        self.fila_emergencia.exibir()
        # Mostra a fila normal.
        print("Fila normal:")
        self.fila_normal.exibir()
        # Mostra quem está nos consultórios.
        print("Em atendimento:")
        self.em_atendimento.exibir()
        # Mostra quantos consultórios estão livres.
        print("Consultórios livres:", self.consultorios_livres())


# ==================== MÓDULO 5: TUTORES E ANIMAIS ====================

# Cria a classe Animal: os dados de um animal cadastrado.
class Animal:
    # Construtor: recebe os dados do animal.
    def __init__(self, nome, especie, raca, idade):
        # Guarda o nome do animal.
        self.nome = nome
        # Guarda a espécie (ex.: cão, gato).
        self.especie = especie
        # Guarda a raça.
        self.raca = raca
        # Guarda a idade em anos.
        self.idade = idade

    # Define como o animal aparece quando é mostrado com print.
    def __str__(self):
        # Monta a frase com os dados do animal.
        return f"{self.nome} - {self.especie}, {self.raca}, {self.idade} ano(s)"


# Cria a classe Tutor: os dados do tutor e a sua própria lista de animais.
class Tutor:
    # Construtor: recebe os dados do tutor.
    def __init__(self, nome, cpf, telefone):
        # Guarda o nome do tutor.
        self.nome = nome
        # Guarda o CPF, que identifica o tutor.
        self.cpf = cpf
        # Guarda o telefone.
        self.telefone = telefone
        # Cria a lista de animais deste tutor, vazia no início e sem limite de tamanho.
        self.animais = ListaEncadeada()

    # Método que procura um animal na lista deste tutor, pelo nome.
    def buscar_animal(self, nome_animal):
        # Começa pelo primeiro animal da lista.
        atual = self.animais.cabeca
        # Percorre a lista de animais enquanto houver nós.
        while atual is not None:
            # Verifica se este é o animal procurado.
            if atual.dado.nome == nome_animal:
                # Devolve o animal encontrado.
                return atual.dado
            # Avança para o próximo animal.
            atual = atual.proximo
        # Se não encontrou, devolve None.
        return None

    # Define como o tutor aparece quando é mostrado com print.
    def __str__(self):
        # Monta a frase com os dados do tutor e quantos animais ele tem.
        return f"{self.nome} (CPF {self.cpf}, tel. {self.telefone}) - {self.animais.tamanho} animal(is)"


# Cria a classe CadastroTutores: a lista de tutores da clínica.
class CadastroTutores:
    # Construtor: cria o cadastro vazio.
    def __init__(self):
        # Cria a lista de tutores, vazia no início.
        self.tutores = ListaEncadeada()

    # Método que procura um tutor pelo CPF.
    def buscar_por_cpf(self, cpf):
        # Começa pelo primeiro tutor da lista.
        atual = self.tutores.cabeca
        # Percorre a lista de tutores enquanto houver nós.
        while atual is not None:
            # Verifica se este é o tutor procurado.
            if atual.dado.cpf == cpf:
                # Devolve o tutor encontrado.
                return atual.dado
            # Avança para o próximo tutor.
            atual = atual.proximo
        # Se não encontrou, devolve None.
        return None

    # Método que cadastra um novo tutor.
    def cadastrar_tutor(self, nome, cpf, telefone):
        # Verifica se já existe um tutor com esse CPF.
        if self.buscar_por_cpf(cpf) is not None:
            # Avisa que o CPF já está cadastrado e não cria outro.
            print(f"Já existe um tutor com o CPF {cpf}.")
            # Devolve None, pois nada foi cadastrado.
            return None
        # Cria o tutor com os dados recebidos.
        tutor = Tutor(nome, cpf, telefone)
        # Insere o tutor no fim da lista de tutores.
        self.tutores.inserir_fim(tutor)
        # Mostra na tela que o cadastro foi feito.
        print(f"Tutor cadastrado: {nome}")
        # Devolve o tutor criado.
        return tutor

    # Método que cadastra um animal para um tutor já existente.
    def cadastrar_animal(self, cpf, nome, especie, raca, idade):
        # Procura o tutor pelo CPF na lista de tutores.
        tutor = self.buscar_por_cpf(cpf)
        # Se o tutor não existir...
        if tutor is None:
            # ...avisa e não cadastra o animal.
            print(f"Tutor com CPF {cpf} não encontrado.")
            # Devolve None, pois nada foi cadastrado.
            return None
        # Cria o animal com os dados recebidos.
        animal = Animal(nome, especie, raca, idade)
        # Insere o animal no fim da lista de animais DESTE tutor.
        tutor.animais.inserir_fim(animal)
        # Mostra na tela que o animal foi cadastrado.
        print(f"Animal cadastrado: {nome}, do tutor {tutor.nome}")
        # Devolve o animal criado.
        return animal

    # Método que busca um animal pelo nome junto com o CPF do tutor.
    # Aqui as duas listas trabalham juntas: primeiro a de tutores, depois a de animais.
    def buscar_animal(self, cpf, nome_animal):
        # Passo 1: percorre a lista de tutores até achar o CPF.
        tutor = self.buscar_por_cpf(cpf)
        # Se o tutor não existir, não há onde procurar o animal.
        if tutor is None:
            # Devolve None.
            return None
        # Passo 2: percorre a lista de animais desse tutor até achar o nome.
        return tutor.buscar_animal(nome_animal)

    # Método que remove um animal de um tutor.
    def remover_animal(self, cpf, nome_animal):
        # Busca o tutor e o animal, usando as duas listas.
        tutor = self.buscar_por_cpf(cpf)
        # Busca o animal na lista desse tutor, se o tutor existir.
        animal = tutor.buscar_animal(nome_animal) if tutor is not None else None
        # Se o animal não foi encontrado...
        if animal is None:
            # ...avisa e não remove nada.
            print(f"Animal {nome_animal} não encontrado para o CPF {cpf}.")
            # Devolve False, pois nada foi removido.
            return False
        # Remove o animal da lista de animais do tutor.
        tutor.animais.remover(animal)
        # Mostra na tela que o animal foi removido.
        print(f"Animal removido: {nome_animal}")
        # Devolve True, pois a remoção deu certo.
        return True

    # Método que remove um tutor e, junto com ele, a sua lista de animais.
    def remover_tutor(self, cpf):
        # Procura o tutor pelo CPF.
        tutor = self.buscar_por_cpf(cpf)
        # Se o tutor não existir...
        if tutor is None:
            # ...avisa e não remove nada.
            print(f"Tutor com CPF {cpf} não encontrado.")
            # Devolve False, pois nada foi removido.
            return False
        # Remove o tutor da lista de tutores; os animais dele saem junto.
        self.tutores.remover(tutor)
        # Mostra na tela que o tutor foi removido.
        print(f"Tutor removido: {tutor.nome}")
        # Devolve True, pois a remoção deu certo.
        return True

    # Método que mostra todos os tutores e, abaixo de cada um, os seus animais.
    def exibir(self):
        # Começa pelo primeiro tutor da lista.
        atual_tutor = self.tutores.cabeca
        # Percorre a lista de tutores.
        while atual_tutor is not None:
            # Mostra os dados do tutor.
            print(atual_tutor.dado)
            # Começa pelo primeiro animal deste tutor.
            atual_animal = atual_tutor.dado.animais.cabeca
            # Percorre a lista de animais deste tutor.
            while atual_animal is not None:
                # Mostra o animal, com recuo para indicar que pertence ao tutor.
                print("   -", atual_animal.dado)
                # Avança para o próximo animal.
                atual_animal = atual_animal.proximo
            # Avança para o próximo tutor.
            atual_tutor = atual_tutor.proximo


# ==================== MÓDULO 6: ÁRVORE DE SISTEMAS DO ANIMAL ====================

# Cria a classe ItemSistema: os dados de um sistema, órgão ou estrutura do animal.
class ItemSistema:
    # Construtor: recebe o nome e, se for um item final, o código.
    def __init__(self, nome, codigo=None):
        # Guarda o nome (ex.: Sistema digestório, Estômago).
        self.nome = nome
        # Guarda o código de identificação; só os itens finais têm código.
        self.codigo = codigo
        # Todo item começa no estado Saudável.
        self.estado = "Saudável"

    # Define como o item aparece quando é mostrado com print.
    def __str__(self):
        # Se o item tem código, mostra o código junto ao nome.
        if self.codigo is not None:
            # Ex.: Estômago (DG01) [Saudável]
            return f"{self.nome} ({self.codigo}) [{self.estado}]"
        # Se não tem código, mostra só o nome e o estado.
        return f"{self.nome} [{self.estado}]"


# Cria a classe ArvoreSistemas: a hierarquia de sistemas usada no diagnóstico.
class ArvoreSistemas:
    # Construtor: cria a árvore com a raiz recebida.
    def __init__(self, nome_raiz):
        # A raiz é o nó do topo da árvore (o animal inteiro).
        self.raiz = NoArvore(ItemSistema(nome_raiz))

    # Método que exibe a árvore indentada, em percurso de profundidade (pré-ordem).
    def exibir(self):
        # Começa o percurso pela raiz, no nível 0 (sem recuo).
        self._exibir_pre_ordem(self.raiz, 0)

    # Método auxiliar recursivo do percurso em pré-ordem.
    def _exibir_pre_ordem(self, no, nivel):
        # PRÉ-ORDEM, passo 1: visita o próprio nó, com recuo conforme o nível.
        print("    " * nivel + "- " + str(no.dado))
        # PRÉ-ORDEM, passo 2: depois visita cada filho, do primeiro ao último.
        filho = no.primeiro_filho
        # Percorre a lista de filhos pelos ponteiros de irmão.
        while filho is not None:
            # Visita o filho (e todos os descendentes dele) um nível abaixo.
            self._exibir_pre_ordem(filho, nivel + 1)
            # Passa para o próximo irmão.
            filho = filho.proximo_irmao

    # Método que procura um item pelo nome ou pelo código.
    def buscar(self, nome_ou_codigo):
        # Começa a busca pela raiz.
        return self._buscar_em(self.raiz, nome_ou_codigo)

    # Método auxiliar recursivo da busca, também em pré-ordem.
    def _buscar_em(self, no, nome_ou_codigo):
        # Verifica se o nó atual é o procurado, pelo nome ou pelo código.
        if no.dado.nome == nome_ou_codigo or no.dado.codigo == nome_ou_codigo:
            # Devolve o nó encontrado.
            return no
        # Se não for, procura em cada filho.
        filho = no.primeiro_filho
        # Percorre a lista de filhos.
        while filho is not None:
            # Procura dentro deste filho e dos descendentes dele.
            encontrado = self._buscar_em(filho, nome_ou_codigo)
            # Se encontrou em algum descendente...
            if encontrado is not None:
                # ...devolve o resultado e para a busca.
                return encontrado
            # Passa para o próximo irmão.
            filho = filho.proximo_irmao
        # Se não encontrou neste ramo, devolve None.
        return None

    # Método que marca um item como Alterado durante o diagnóstico.
    def marcar_alterado(self, nome_ou_codigo):
        # Procura o item na árvore.
        no = self.buscar(nome_ou_codigo)
        # Se não encontrou...
        if no is None:
            # ...avisa e não marca nada.
            print(f"Item {nome_ou_codigo} não encontrado na árvore.")
            # Devolve False, pois nada foi marcado.
            return False
        # Muda o estado do item para Alterado.
        no.dado.estado = "Alterado"
        # Mostra na tela qual item foi marcado.
        print(f"Marcado como Alterado: {no.dado.nome}")
        # Devolve True, pois a marcação deu certo.
        return True

    # Método que devolve uma lista com todos os itens marcados como Alterado.
    def itens_alterados(self):
        # Cria a lista encadeada que vai receber os itens alterados.
        resultado = ListaEncadeada()
        # Percorre a árvore a partir da raiz, preenchendo a lista.
        self._coletar_alterados(self.raiz, resultado)
        # Devolve a lista; ela será usada no prontuário.
        return resultado

    # Método auxiliar recursivo que junta os itens alterados, em pré-ordem.
    def _coletar_alterados(self, no, resultado):
        # Se o item do nó atual está alterado...
        if no.dado.estado == "Alterado":
            # ...coloca o item na lista de resultado.
            resultado.inserir_fim(no.dado)
        # Depois visita cada filho.
        filho = no.primeiro_filho
        # Percorre a lista de filhos.
        while filho is not None:
            # Junta os alterados deste filho e dos descendentes dele.
            self._coletar_alterados(filho, resultado)
            # Passa para o próximo irmão.
            filho = filho.proximo_irmao


# Função que monta a árvore pré-definida de sistemas do animal.
def criar_arvore_sistemas():
    # Cria a árvore com a raiz "Animal".
    arvore = ArvoreSistemas("Animal")
    # Guarda a raiz para pendurar os sistemas nela.
    animal = arvore.raiz

    # Acrescenta o sistema digestório como filho da raiz.
    digestorio = animal.adicionar_filho(ItemSistema("Sistema digestório"))
    # Acrescenta a boca, que por sua vez tem partes menores.
    boca = digestorio.adicionar_filho(ItemSistema("Boca"))
    # Partes da boca: itens finais, com código.
    boca.adicionar_filho(ItemSistema("Dentes", "DG01"))
    boca.adicionar_filho(ItemSistema("Gengiva", "DG02"))
    # Demais órgãos do sistema digestório.
    digestorio.adicionar_filho(ItemSistema("Estômago", "DG03"))
    digestorio.adicionar_filho(ItemSistema("Intestino", "DG04"))

    # Acrescenta o sistema respiratório e seus órgãos.
    respiratorio = animal.adicionar_filho(ItemSistema("Sistema respiratório"))
    respiratorio.adicionar_filho(ItemSistema("Pulmões", "RS01"))
    respiratorio.adicionar_filho(ItemSistema("Traqueia", "RS02"))

    # Acrescenta a pele e suas estruturas.
    pele = animal.adicionar_filho(ItemSistema("Pele"))
    pele.adicionar_filho(ItemSistema("Pelos", "PL01"))
    pele.adicionar_filho(ItemSistema("Unhas", "PL02"))

    # Acrescenta o sistema locomotor e suas estruturas.
    locomotor = animal.adicionar_filho(ItemSistema("Sistema locomotor"))
    locomotor.adicionar_filho(ItemSistema("Patas dianteiras", "LC01"))
    locomotor.adicionar_filho(ItemSistema("Patas traseiras", "LC02"))
    locomotor.adicionar_filho(ItemSistema("Coluna", "LC03"))

    # Devolve a árvore pronta.
    return arvore


# ==================== MÓDULO 7: ESTOQUE DE MEDICAMENTOS E VACINAS ====================

# Cria a classe Lote: uma compra de um produto, com datas e preços próprios.
class Lote:
    # Construtor: recebe os dados da compra.
    def __init__(self, fornecedor, preco_compra, preco_venda, data_compra, validade, quantidade):
        # Guarda o fornecedor deste lote.
        self.fornecedor = fornecedor
        # Guarda o preço pago por unidade.
        self.preco_compra = preco_compra
        # Guarda o preço cobrado do tutor por unidade.
        self.preco_venda = preco_venda
        # Guarda a data da compra.
        self.data_compra = data_compra
        # Guarda a data de validade.
        self.validade = validade
        # Guarda quantas unidades restam neste lote.
        self.quantidade = quantidade

    # Método que responde se o lote está vencido numa certa data.
    def vencido(self, data_referencia):
        # Está vencido se a validade já passou.
        return self.validade < data_referencia

    # Define como o lote aparece quando é mostrado com print.
    def __str__(self):
        # Monta a frase com os dados principais do lote.
        return (f"lote de {self.data_compra.strftime('%d/%m/%Y')} ({self.fornecedor}) - "
                f"{self.quantidade} un. - validade {self.validade.strftime('%d/%m/%Y')} - "
                f"R$ {self.preco_venda:.2f}/un.")


# Cria a classe Produto: um item do estoque, com a sua própria fila de lotes.
class Produto:
    # Construtor: recebe os dados fixos do produto.
    def __init__(self, codigo, nome, minimo, destino_descarte):
        # Guarda o código do produto.
        self.codigo = codigo
        # Guarda o nome do produto.
        self.nome = nome
        # Guarda a quantidade mínima; abaixo dela o sistema emite alerta.
        self.minimo = minimo
        # Guarda o destino correto de descarte, conforme as normas de resíduos de saúde.
        self.destino_descarte = destino_descarte
        # Cria a fila de lotes: o primeiro lote comprado é o primeiro a sair.
        self.lotes = Fila()

    # Método que soma a quantidade de todos os lotes do produto.
    def quantidade_total(self):
        # Começa a soma em zero.
        total = 0
        # Começa pelo primeiro lote da fila.
        atual = self.lotes.inicio
        # Percorre todos os lotes.
        while atual is not None:
            # Soma a quantidade deste lote.
            total += atual.dado.quantidade
            # Avança para o próximo lote.
            atual = atual.proximo
        # Devolve o total.
        return total

    # Define como o produto aparece quando é mostrado com print.
    def __str__(self):
        # Monta a frase com código, nome, total e mínimo.
        return f"{self.codigo} - {self.nome}: {self.quantidade_total()} un. (mínimo {self.minimo})"


# Cria a classe Perda: o registro de um lote descartado por vencimento.
class Perda:
    # Construtor: recebe os dados do lote descartado.
    def __init__(self, produto, lote, data_descarte):
        # Guarda o nome do produto.
        self.nome_produto = produto.nome
        # Guarda quantas unidades foram perdidas.
        self.quantidade = lote.quantidade
        # Guarda o valor perdido, pelo preço de compra.
        self.valor = lote.quantidade * lote.preco_compra
        # Guarda a validade do lote.
        self.validade = lote.validade
        # Guarda a data em que o descarte foi registrado.
        self.data_descarte = data_descarte
        # Guarda para onde o material foi encaminhado.
        self.destino = produto.destino_descarte

    # Define como a perda aparece quando é mostrada com print.
    def __str__(self):
        # Monta a frase com os dados da perda.
        return (f"{self.nome_produto}: {self.quantidade} un. vencidas em "
                f"{self.validade.strftime('%d/%m/%Y')} - perda de R$ {self.valor:.2f} - "
                f"destino: {self.destino}")


# Cria a classe Estoque: a lista de produtos e a lista de perdas da clínica.
class Estoque:
    # Construtor: cria o estoque vazio.
    def __init__(self):
        # Cria a lista de produtos, cada um com a sua fila de lotes.
        self.produtos = ListaEncadeada()
        # Cria a lista de perdas por vencimento.
        self.perdas = ListaEncadeada()

    # Método que procura um produto pelo código, percorrendo a lista de produtos.
    def buscar_produto(self, codigo):
        # Começa pelo primeiro produto.
        atual = self.produtos.cabeca
        # Percorre a lista de produtos.
        while atual is not None:
            # Verifica se este é o produto procurado.
            if atual.dado.codigo == codigo:
                # Devolve o produto encontrado.
                return atual.dado
            # Avança para o próximo produto.
            atual = atual.proximo
        # Se não encontrou, devolve None.
        return None

    # Método que cadastra um produto novo, ainda sem lotes.
    def cadastrar_produto(self, codigo, nome, minimo, destino_descarte):
        # Verifica se o código já existe.
        if self.buscar_produto(codigo) is not None:
            # Avisa e não cadastra de novo.
            print(f"Produto {codigo} já cadastrado.")
            # Devolve None, pois nada foi cadastrado.
            return None
        # Cria o produto.
        produto = Produto(codigo, nome, minimo, destino_descarte)
        # Insere o produto no fim da lista de produtos.
        self.produtos.inserir_fim(produto)
        # Devolve o produto criado.
        return produto

    # Método que registra a entrada de um lote comprado.
    def entrada_lote(self, codigo, fornecedor, preco_compra, preco_venda, data_compra, validade, quantidade):
        # Procura o produto na lista de produtos.
        produto = self.buscar_produto(codigo)
        # Se o produto não existir...
        if produto is None:
            # ...avisa e não registra o lote.
            print(f"Produto {codigo} não encontrado.")
            # Devolve False.
            return False
        # Cria o lote com os dados da compra.
        lote = Lote(fornecedor, preco_compra, preco_venda, data_compra, validade, quantidade)
        # Coloca o lote no FIM da fila: ele será o último a sair.
        produto.lotes.enfileirar(lote)
        # Mostra na tela a entrada registrada.
        print(f"Entrada: {produto.nome}, {lote}")
        # Devolve True.
        return True

    # Método que descarta os lotes vencidos de todos os produtos e registra as perdas.
    def descartar_vencidos(self, data_referencia=None):
        # Se nenhuma data for informada, usa a data de hoje.
        if data_referencia is None:
            data_referencia = date.today()
        # Começa pelo primeiro produto.
        atual = self.produtos.cabeca
        # Percorre a lista de produtos.
        while atual is not None:
            # Descarta os vencidos deste produto.
            self._descartar_vencidos_produto(atual.dado, data_referencia)
            # Avança para o próximo produto.
            atual = atual.proximo

    # Método auxiliar que descarta os lotes vencidos de um único produto.
    def _descartar_vencidos_produto(self, produto, data_referencia):
        # Cada lote sai da fila uma vez; por isso guardamos quantos há agora.
        quantidade_lotes = produto.lotes.tamanho
        # Repete uma vez para cada lote.
        for _ in range(quantidade_lotes):
            # Tira o lote do início da fila.
            lote = produto.lotes.desenfileirar()
            # Se estiver vencido...
            if lote.vencido(data_referencia):
                # ...registra a perda na lista de perdas.
                perda = Perda(produto, lote, data_referencia)
                self.perdas.inserir_fim(perda)
                # Mostra na tela o descarte.
                print(f"DESCARTE: {perda}")
            # Se ainda estiver válido...
            else:
                # ...volta para o fim da fila; como todos passam uma vez, a ordem se mantém.
                produto.lotes.enfileirar(lote)

    # Método que retira unidades de um produto, sempre do lote mais antigo.
    # Devolve o valor de venda das unidades retiradas, ou None se não houver estoque.
    def retirar(self, codigo, quantidade, data_referencia=None):
        # Se nenhuma data for informada, usa a data de hoje.
        if data_referencia is None:
            data_referencia = date.today()
        # Procura o produto na lista de produtos.
        produto = self.buscar_produto(codigo)
        # Se o produto não existir...
        if produto is None:
            # ...avisa e não retira nada.
            print(f"Produto {codigo} não encontrado.")
            # Devolve None.
            return None
        # Antes de retirar, descarta os vencidos deste produto, para nunca usar lote vencido.
        self._descartar_vencidos_produto(produto, data_referencia)
        # Verifica se há quantidade suficiente.
        if produto.quantidade_total() < quantidade:
            # Avisa que o estoque não é suficiente.
            print(f"Estoque insuficiente de {produto.nome}: há {produto.quantidade_total()}, pedido {quantidade}.")
            # Devolve None, pois nada foi retirado.
            return None
        # Guarda quanto ainda falta retirar.
        falta = quantidade
        # Começa o valor da retirada em zero.
        valor = 0
        # Repete enquanto ainda faltar retirar.
        while falta > 0:
            # Olha o lote mais antigo, no início da fila, sem tirá-lo.
            lote = produto.lotes.espiar()
            # Se o lote tem menos do que falta, usa o lote inteiro.
            if lote.quantidade <= falta:
                # Soma o valor das unidades deste lote.
                valor += lote.quantidade * lote.preco_venda
                # Diminui o que falta.
                falta -= lote.quantidade
                # O lote acabou: sai da fila.
                produto.lotes.desenfileirar()
            # Se o lote tem mais do que falta, usa só uma parte dele.
            else:
                # Soma o valor das unidades usadas.
                valor += falta * lote.preco_venda
                # Diminui a quantidade restante no lote.
                lote.quantidade -= falta
                # Não falta mais nada.
                falta = 0
        # Mostra na tela a retirada.
        print(f"Retirada: {quantidade} un. de {produto.nome} - R$ {valor:.2f}")
        # Confere se o produto ficou abaixo do mínimo.
        self.verificar_minimo(produto)
        # Devolve o valor de venda das unidades retiradas.
        return valor

    # Método de ajuste de inventário: corrige o total de um produto após contagem física.
    def ajustar_quantidade(self, codigo, nova_quantidade):
        # Procura o produto.
        produto = self.buscar_produto(codigo)
        # Se não existir ou não tiver lotes, não há o que ajustar.
        if produto is None or produto.lotes.esta_vazia():
            # Avisa.
            print(f"Não é possível ajustar o produto {codigo}.")
            # Devolve False.
            return False
        # Calcula a diferença entre a contagem física e o sistema.
        diferenca = nova_quantidade - produto.quantidade_total()
        # Se sobrou produto na contagem, soma a diferença ao lote mais novo.
        if diferenca > 0:
            # O lote mais novo é o último da fila.
            produto.lotes.fim.dado.quantidade += diferenca
        # Se faltou produto na contagem, tira a diferença começando pelo lote mais antigo.
        elif diferenca < 0:
            # Guarda quanto falta tirar.
            falta = -diferenca
            # Repete enquanto faltar.
            while falta > 0:
                # Olha o lote mais antigo.
                lote = produto.lotes.espiar()
                # Se o lote tem menos do que falta, ele zera e sai da fila.
                if lote.quantidade <= falta:
                    falta -= lote.quantidade
                    produto.lotes.desenfileirar()
                # Se tem mais, só diminui a quantidade.
                else:
                    lote.quantidade -= falta
                    falta = 0
        # Mostra na tela o ajuste feito.
        print(f"Ajuste de inventário: {produto.nome} agora com {produto.quantidade_total()} un.")
        # Confere se o produto ficou abaixo do mínimo.
        self.verificar_minimo(produto)
        # Devolve True.
        return True

    # Método que emite alerta se o total de um produto estiver abaixo do mínimo.
    def verificar_minimo(self, produto):
        # Compara o total com o mínimo.
        if produto.quantidade_total() < produto.minimo:
            # Emite o alerta de reposição.
            print(f"ALERTA: {produto.nome} abaixo do mínimo "
                  f"({produto.quantidade_total()} de {produto.minimo}). Providenciar reposição.")

    # Método que avisa quais lotes vencem nos próximos dias.
    def alerta_vencimento_proximo(self, dias=30, data_referencia=None):
        # Se nenhuma data for informada, usa a data de hoje.
        if data_referencia is None:
            data_referencia = date.today()
        # Calcula a data limite do aviso.
        limite = data_referencia + timedelta(days=dias)
        # Começa pelo primeiro produto.
        atual_produto = self.produtos.cabeca
        # Percorre a lista de produtos.
        while atual_produto is not None:
            # Começa pelo primeiro lote deste produto.
            atual_lote = atual_produto.dado.lotes.inicio
            # Percorre a fila de lotes sem tirar ninguém dela.
            while atual_lote is not None:
                # Pega o lote.
                lote = atual_lote.dado
                # Se ainda vale mas vence até o limite...
                if data_referencia <= lote.validade <= limite:
                    # ...emite o aviso.
                    print(f"AVISO: {atual_produto.dado.nome}, {lote} - vence em até {dias} dias.")
                # Avança para o próximo lote.
                atual_lote = atual_lote.proximo
            # Avança para o próximo produto.
            atual_produto = atual_produto.proximo

    # Método que mostra todos os produtos e, abaixo de cada um, os seus lotes.
    def exibir(self):
        # Começa pelo primeiro produto.
        atual_produto = self.produtos.cabeca
        # Percorre a lista de produtos.
        while atual_produto is not None:
            # Mostra o produto.
            print(atual_produto.dado)
            # Mostra os lotes do produto, do mais antigo ao mais novo.
            atual_lote = atual_produto.dado.lotes.inicio
            # Percorre a fila de lotes.
            while atual_lote is not None:
                # Mostra o lote com recuo.
                print("   -", atual_lote.dado)
                # Avança para o próximo lote.
                atual_lote = atual_lote.proximo
            # Avança para o próximo produto.
            atual_produto = atual_produto.proximo
