# Este arquivo guarda as estruturas de dados genéricas do projeto.
# Elas não sabem nada sobre a clínica e podem ser usadas em qualquer sistema.


# ==================== MÓDULO 1: NÓ ====================

# Cria a classe No, o "tijolo" básico das estruturas encadeadas.
class No:
    # Construtor: roda automaticamente quando um nó novo é criado.
    def __init__(self, dado):
        # Guarda dentro do nó a informação recebida (ex.: o nome de um animal).
        self.dado = dado
        # Cria o ponteiro para o próximo nó; começa sem apontar para ninguém.
        self.proximo = None


# ==================== MÓDULO 2: LISTA ENCADEADA ====================

# Cria a classe ListaEncadeada, que liga vários nós em sequência.
class ListaEncadeada:
    # Construtor: cria uma lista nova, ainda vazia.
    def __init__(self):
        # Ponteiro para o primeiro nó da lista; vazio no início.
        self.cabeca = None
        # Ponteiro para o último nó da lista; vazio no início.
        self.cauda = None
        # Contador de quantos nós a lista tem.
        self.tamanho = 0

    # Método que responde se a lista está vazia.
    def esta_vazia(self):
        # Devolve True se não houver primeiro nó, e False se houver.
        return self.cabeca is None

    # Método que insere um novo dado no fim da lista.
    def inserir_fim(self, dado):
        # Cria um nó novo contendo o dado recebido.
        novo = No(dado)
        # Verifica se a lista está vazia.
        if self.esta_vazia():
            # Se estiver vazia, o novo nó passa a ser o primeiro...
            self.cabeca = novo
            # ...e também o último, pois é o único nó.
            self.cauda = novo
        # Caso a lista já tenha nós.
        else:
            # O último nó atual passa a apontar para o novo nó.
            self.cauda.proximo = novo
            # O novo nó passa a ser o último da lista.
            self.cauda = novo
        # Aumenta em 1 o contador de nós.
        self.tamanho += 1

    # Método que mostra na tela todos os dados da lista, do primeiro ao último.
    def exibir(self):
        # Começa a caminhada pelo primeiro nó.
        atual = self.cabeca
        # Repete enquanto ainda houver nó para visitar.
        while atual is not None:
            # Mostra o dado do nó atual.
            print(atual.dado)
            # Avança para o próximo nó seguindo o ponteiro.
            atual = atual.proximo

    # Método que remove da lista o primeiro nó que contém o dado informado.
    def remover(self, dado):
        # Guarda o nó que vem antes do atual; no início não há nenhum.
        anterior = None
        # Começa a busca pelo primeiro nó da lista.
        atual = self.cabeca
        # Repete enquanto ainda houver nó para visitar.
        while atual is not None:
            # Verifica se o nó atual contém o dado procurado.
            if atual.dado == dado:
                # Se não há anterior, o nó a remover é o primeiro da lista...
                if anterior is None:
                    # ...então a cabeça passa a ser o segundo nó.
                    self.cabeca = atual.proximo
                # Se há anterior, o nó a remover está no meio ou no fim...
                else:
                    # ...então o anterior "pula" o atual e aponta para o seguinte.
                    anterior.proximo = atual.proximo
                # Verifica se o nó removido era o último da lista.
                if atual is self.cauda:
                    # Se era, a cauda passa a ser o nó anterior.
                    self.cauda = anterior
                # Diminui em 1 o contador de nós.
                self.tamanho -= 1
                # Avisa que a remoção deu certo.
                return True
            # Antes de avançar, o atual vira o anterior.
            anterior = atual
            # Avança para o próximo nó seguindo o ponteiro.
            atual = atual.proximo
        # Se percorreu tudo e não achou, avisa que nada foi removido.
        return False


# ==================== MÓDULO 3: FILA ====================

# Cria a classe Fila: o primeiro a entrar é o primeiro a sair (FIFO).
class Fila:
    # Construtor: cria uma fila nova, ainda vazia.
    def __init__(self):
        # Ponteiro para o primeiro da fila (o próximo a ser atendido).
        self.inicio = None
        # Ponteiro para o último da fila (onde os novos entram).
        self.fim = None
        # Contador de quantos itens estão na fila.
        self.tamanho = 0

    # Método que responde se a fila está vazia.
    def esta_vazia(self):
        # Devolve True se não houver ninguém no início da fila.
        return self.inicio is None

    # Método que coloca um novo item no fim da fila. Custo O(1).
    def enfileirar(self, dado):
        # Cria um nó novo contendo o dado recebido.
        novo = No(dado)
        # Verifica se a fila está vazia.
        if self.esta_vazia():
            # Se estiver vazia, o novo nó é ao mesmo tempo o início...
            self.inicio = novo
            # ...e o fim da fila.
            self.fim = novo
        # Caso a fila já tenha itens.
        else:
            # O último da fila passa a apontar para o novo nó.
            self.fim.proximo = novo
            # O novo nó passa a ser o último da fila.
            self.fim = novo
        # Aumenta em 1 o contador da fila.
        self.tamanho += 1

    # Método que tira e devolve o primeiro item da fila. Custo O(1).
    def desenfileirar(self):
        # Se a fila estiver vazia, não há quem tirar.
        if self.esta_vazia():
            # Devolve None para indicar que não havia ninguém.
            return None
        # Guarda o nó que está no início da fila.
        primeiro = self.inicio
        # O início passa a ser o segundo da fila.
        self.inicio = primeiro.proximo
        # Se a fila ficou vazia depois da saída...
        if self.inicio is None:
            # ...o fim também deixa de apontar para alguém.
            self.fim = None
        # Diminui em 1 o contador da fila.
        self.tamanho -= 1
        # Devolve o dado de quem saiu da fila.
        return primeiro.dado

    # Método que mostra quem é o primeiro da fila, sem tirá-lo. Custo O(1).
    def espiar(self):
        # Se a fila estiver vazia, não há ninguém para mostrar.
        if self.esta_vazia():
            # Devolve None para indicar que a fila está vazia.
            return None
        # Devolve o dado do primeiro da fila, que continua no lugar.
        return self.inicio.dado

    # Método que mostra na tela todos os itens da fila, do início ao fim.
    def exibir(self):
        # Começa pelo primeiro da fila.
        atual = self.inicio
        # Repete enquanto ainda houver item para visitar.
        while atual is not None:
            # Mostra o dado do item atual.
            print(atual.dado)
            # Avança para o próximo item seguindo o ponteiro.
            atual = atual.proximo


# ==================== MÓDULO 6: NÓ DE ÁRVORE N-ÁRIA ====================

# Cria a classe NoArvore: um nó de árvore que pode ter de zero a N filhos.
# A árvore não é binária nem de busca. Os filhos de cada nó formam uma
# lista encadeada, ligada pelos ponteiros primeiro_filho e proximo_irmao.
class NoArvore:
    # Construtor: roda quando um nó de árvore novo é criado.
    def __init__(self, dado):
        # Guarda dentro do nó a informação recebida.
        self.dado = dado
        # Ponteiro para o primeiro filho deste nó; começa sem filhos.
        self.primeiro_filho = None
        # Ponteiro para o próximo irmão (o filho seguinte do mesmo pai).
        self.proximo_irmao = None

    # Método que acrescenta um filho no fim da lista de filhos deste nó.
    def adicionar_filho(self, dado):
        # Cria o nó do novo filho.
        novo = NoArvore(dado)
        # Se este nó ainda não tem filhos...
        if self.primeiro_filho is None:
            # ...o novo nó passa a ser o primeiro filho.
            self.primeiro_filho = novo
        # Se já tem filhos...
        else:
            # ...começa pelo primeiro filho...
            atual = self.primeiro_filho
            # ...e anda pelos irmãos até chegar ao último.
            while atual.proximo_irmao is not None:
                # Avança para o próximo irmão.
                atual = atual.proximo_irmao
            # O último irmão passa a apontar para o novo filho.
            atual.proximo_irmao = novo
        # Devolve o novo nó, para que ele também possa receber filhos.
        return novo


# ==================== MÓDULO 8: PILHA ====================

# Cria a classe Pilha: o último a entrar é o primeiro a sair (LIFO).
class Pilha:
    # Construtor: cria uma pilha nova, ainda vazia.
    def __init__(self):
        # Ponteiro para o item do topo da pilha; vazio no início.
        self.topo = None
        # Contador de quantos itens estão na pilha.
        self.tamanho = 0

    # Método que responde se a pilha está vazia.
    def esta_vazia(self):
        # Devolve True se não houver ninguém no topo.
        return self.topo is None

    # Método que coloca um novo item no topo da pilha. Custo O(1).
    def empilhar(self, dado):
        # Cria um nó novo contendo o dado recebido.
        novo = No(dado)
        # O novo nó aponta para o antigo topo.
        novo.proximo = self.topo
        # O novo nó passa a ser o topo.
        self.topo = novo
        # Aumenta em 1 o contador.
        self.tamanho += 1

    # Método que tira e devolve o item do topo da pilha. Custo O(1).
    def desempilhar(self):
        # Se a pilha estiver vazia, não há o que tirar.
        if self.esta_vazia():
            # Devolve None para indicar que estava vazia.
            return None
        # Guarda o nó do topo.
        removido = self.topo
        # O topo passa a ser o nó de baixo.
        self.topo = removido.proximo
        # Diminui em 1 o contador.
        self.tamanho -= 1
        # Devolve o dado de quem saiu.
        return removido.dado

    # Método que mostra o item do topo, sem tirá-lo. Custo O(1).
    def espiar(self):
        # Se a pilha estiver vazia, devolve None.
        if self.esta_vazia():
            return None
        # Devolve o dado do topo.
        return self.topo.dado
