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
