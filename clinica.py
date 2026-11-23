# Este arquivo guarda as regras da Clínica Veterinária.
# Ele usa as estruturas genéricas do arquivo estruturas.py, mas não as modifica.

# Traz a lista encadeada e a fila que criamos nos módulos anteriores.
from estruturas import ListaEncadeada, Fila
# Traz a biblioteca de datas do Python, usada só para registrar data e hora.
from datetime import datetime


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
