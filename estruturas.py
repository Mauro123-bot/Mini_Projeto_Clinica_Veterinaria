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
