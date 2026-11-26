# Projeto Clínica Veterinária

## Vídeo de apresentação

https://youtu.be/T1GFcxsd6ZM

Disciplina Estrutura de Dados, Fatec Rio Claro. Prof. Orlando.

## 1. Concepção do projeto

Este projeto desenvolve, em Python, um mini sistema de gestão para uma clínica veterinária. Ele segue o mesmo raciocínio do projeto anterior da disciplina, a Oficina Mecânica Sustentável, aplicado a um novo contexto. Onde a oficina atendia veículos, a clínica atende animais. Onde a oficina tinha boxes, a clínica tem consultórios.

O sistema gerencia o ciclo completo de um atendimento. O animal chega e entra na espera, com prioridade para emergências. Quando um consultório fica livre, o próximo animal é chamado e o prontuário é aberto. O veterinário faz o diagnóstico numa árvore de sistemas do animal, marcando os itens alterados. Medicamentos e procedimentos entram no prontuário ao longo do atendimento. Após a alta, o prontuário é fechado, o estoque é baixado pelo lote mais antigo, o pagamento é registrado e o sistema anota o que cada animal consumiu.

Todas as estruturas de dados foram implementadas em classes próprias. Não usamos list nem dict do Python para guardar os dados do problema. A única biblioteca usada é datetime, para datas e horários.

## 2. Como executar

```
python main.py
```

Roda os testes de cada módulo em sequência e termina com a simulação completa de um atendimento.

```
python main.py simulacao
```

Roda apenas a simulação completa.

## 3. Organização do código

O código está separado em três arquivos. As estruturas de dados genéricas não sabem nada sobre a clínica. As regras da clínica usam essas estruturas sem modificá-las.

| Arquivo | Conteúdo |
|---|---|
| `estruturas.py` | Estruturas de dados genéricas |
| `clinica.py` | Regras da clínica |
| `main.py` | Testes de cada módulo e chamada da simulação |

### Estruturas genéricas (`estruturas.py`)

| Módulo | Classe | Comportamento |
|---|---|---|
| 1 | `No` | Guarda um dado e o ponteiro para o próximo nó |
| 2 | `ListaEncadeada` | Inserção no fim, remoção em qualquer posição, percurso |
| 3 | `Fila` | Primeiro a entrar, primeiro a sair (FIFO) |
| 6 | `NoArvore` | Nó de árvore N-ária, com `primeiro_filho` e `proximo_irmao` |
| 8 | `Pilha` | Último a entrar, primeiro a sair (LIFO) |

### Regras da clínica (`clinica.py`)

| Módulo | Classes | Responsabilidade |
|---|---|---|
| 4 | `Atendimento`, `ControleAtendimento` | Espera dos animais e ocupação dos consultórios |
| 5 | `Animal`, `Tutor`, `CadastroTutores` | Tutores e seus animais |
| 6 | `ItemSistema`, `ArvoreSistemas` | Árvore de sistemas do animal e diagnóstico |
| 7 | `Lote`, `Produto`, `Perda`, `Estoque` | Estoque com lotes, validade, descarte e alertas |
| 8 | `ItemMedicamento`, `Procedimento`, `Prontuario`, `ControleProntuarios` | Prontuários de atendimento |
| 9 | `Pagamento` | Dados de cada pagamento |
| 10 | `RegistroConsumo`, `Caixa` | Fechamento do prontuário, baixa no estoque e consumo |
| 11 | `criar_arvore_sistemas`, `simular_atendimento_completo` | Árvore pré-definida e simulação do fluxo completo |

## 4. Árvore de sistemas do animal

A árvore é N-ária, ou seja, cada nó pode ter de 0 a N filhos. Ela não é binária nem de busca. Os filhos de cada nó ficam numa lista encadeada, com os ponteiros `primeiro_filho` e `proximo_irmao`. A árvore é pré-definida pela função `criar_arvore_sistemas()`.

```
Animal
├── Sistema digestório
│   ├── Boca
│   │   ├── Dentes (DG01)
│   │   └── Gengiva (DG02)
│   ├── Estômago (DG03)
│   └── Intestino (DG04)
├── Sistema respiratório
│   ├── Pulmões (RS01)
│   └── Traqueia (RS02)
├── Pele
│   ├── Pelos (PL01)
│   └── Unhas (PL02)
└── Sistema locomotor
    ├── Patas dianteiras (LC01)
    ├── Patas traseiras (LC02)
    └── Coluna (LC03)
```

Cada nó guarda o nome do sistema, órgão ou estrutura, o código de identificação quando for um item final e o estado, que pode ser "Saudável" ou "Alterado". A exibição usa percurso em profundidade, em pré-ordem, com recuo para mostrar a hierarquia.

## 5. Combinações de estruturas

### 5.1 Atendimento com prioridade: Fila + Fila

**Classes e métodos.** `ControleAtendimento` tem duas `Fila`, `fila_emergencia` e `fila_normal`. As filas trabalham juntas em `registrar_chegada`, `proximo_da_vez`, `chamar_proximo` e `liberar_consultorio`. Os animais em atendimento ficam numa `ListaEncadeada`.

**Por que é adequada.** Cada fila mantém a ordem de chegada entre os animais do mesmo tipo, como pede o enunciado. O próximo atendido vem da fila de emergência. Se ela estiver vazia, vem da fila normal. Quando um consultório fica livre, `liberar_consultorio` chama o próximo automaticamente.

**Desvantagem de usar uma estrutura só.** Numa fila única, uma emergência precisaria ser inserida no meio, à frente dos casos normais. Isso exige percorrer a fila a cada chegada, com custo O(n), e descaracteriza a fila. Com uma fila por prioridade, chegar e ser chamado custam O(1).

### 5.2 Tutores e seus animais: Lista + Lista

**Classes e métodos.** `CadastroTutores` tem uma `ListaEncadeada` de `Tutor`, e cada tutor tem a sua própria `ListaEncadeada` de `Animal`. As duas listas trabalham juntas em `buscar_animal`, `cadastrar_animal` e `remover_animal`.

**Por que é adequada.** Um tutor pode ter quantos animais quiser, sem limite pré-definido. A lista cresce conforme novos animais são cadastrados. Na busca, o sistema percorre a lista de tutores até o CPF e, em seguida, a lista de animais daquele tutor.

**Desvantagem de usar uma estrutura só.** Numa lista única de animais, cada animal precisaria repetir os dados do tutor. Isso duplica informação e permite inconsistências, como o mesmo CPF com telefones diferentes.

### 5.3 Estoque com vários lotes: Lista de produtos, cada um com uma Fila de lotes

**Classes e métodos.** `Estoque` tem uma `ListaEncadeada` de `Produto`, e cada produto tem uma `Fila` de `Lote`. As estruturas trabalham juntas em `buscar_produto`, `entrada_lote`, `retirar`, `descartar_vencidos` e `ajustar_quantidade`.

**Por que é adequada.** Um mesmo produto pode ter lotes comprados em datas e preços diferentes. A fila garante que a saída sempre consuma primeiro o lote mais antigo, como pede o enunciado. Em `descartar_vencidos`, cada lote sai da fila uma vez. Os vencidos são registrados como perda e os válidos voltam para o fim, o que mantém a ordem original.

**Desvantagem de usar uma estrutura só.** Se todos os lotes de todos os produtos ficassem numa única fila, para tirar amoxicilina seria preciso passar por vacinas e seringas até achar o lote certo. Com uma fila por produto, o lote certo está sempre no início.

### 5.4 Árvore de sistemas: Árvore + Lista

**Classes e métodos.** Em `NoArvore`, os filhos de cada nó formam uma lista encadeada pelos ponteiros `primeiro_filho` e `proximo_irmao`. O método `itens_alterados` percorre a árvore em pré-ordem e devolve uma `ListaEncadeada` com os itens marcados como alterados.

**Por que é adequada.** A lista de filhos permite que cada nó tenha qualquer quantidade de filhos. A lista de alterados é o elo entre o diagnóstico e o prontuário.

**Desvantagem de usar uma estrutura só.** Uma árvore binária limitaria cada nó a dois filhos, e o enunciado exige de 0 a N.

### 5.5 Prontuário: Lista de medicamentos + Lista de procedimentos + Pilha de inclusões

**Classes e métodos.** Cada `Prontuario` tem duas `ListaEncadeada`, uma de `ItemMedicamento` e outra de `Procedimento`, e uma `Pilha` chamada `historico`. Os métodos envolvidos são `adicionar_medicamento`, `adicionar_procedimento`, `remover_medicamento`, `remover_procedimento` e `desfazer_ultima_inclusao`.

**Por que é adequada.** Medicamentos e procedimentos entram e saem em qualquer posição, conforme o diagnóstico avança ou o tutor não autoriza um procedimento, e a lista permite isso. A pilha guarda as inclusões na ordem em que aconteceram, e desfazer a última é exatamente o comportamento LIFO.

**Desvantagem de usar uma estrutura só.** Uma lista sozinha não saberia qual item foi incluído por último. Seria preciso controlar isso à mão.

### 5.6 Fechamento: Prontuário + Estoque + Caixa

**Classes e métodos.** `Caixa.fechar_e_pagar` percorre a lista de medicamentos do prontuário, busca cada um na lista de produtos do `Estoque` e consome a fila de lotes daquele produto. No mesmo passo, cria um `RegistroConsumo` para cada item, registra o `Pagamento` e fecha o prontuário. O caixa guarda pagamentos e consumos em listas, e `consumo_por_animal` mostra o que cada animal consumiu.

**Por que é adequada.** O método `estoque_suficiente` confere todos os itens antes de baixar qualquer um. Assim o estoque nunca fica pela metade se faltar algum item. A baixa acontece no fechamento, e não na inclusão, para que o tutor possa desistir de um medicamento sem que o estoque precise ser corrigido.

**Desvantagem de usar uma estrutura só.** Guardar pagamento e consumo dentro do próprio prontuário misturaria responsabilidades e dificultaria consultar o consumo de um animal em vários prontuários.

## 6. Complexidade das principais operações

| Operação | Complexidade |
|---|---|
| Inserir no fim da lista encadeada | O(1), graças ao ponteiro `cauda` |
| Remover da lista encadeada | O(n) |
| Enfileirar, desenfileirar e espiar na fila | O(1) |
| Empilhar, desempilhar e espiar na pilha | O(1) |
| Chamar o próximo animal | O(1) |
| Buscar tutor por CPF | O(t), com t tutores |
| Buscar animal por CPF e nome | O(t + a), com a animais do tutor |
| Buscar produto no estoque | O(p), com p produtos |
| Descartar lotes vencidos | O(p + l), com l lotes no total |
| Exibir, buscar ou marcar na árvore | O(k), com k nós |

## 7. Sustentabilidade

**Ambiental.** Cada produto do estoque guarda o destino correto de descarte, conforme as normas para resíduos de serviços de saúde. Medicamentos vencidos são resíduo químico, vacinas são resíduo biológico e seringas com agulha são perfurocortantes, descartadas em caixa rígida própria. Lotes vencidos são registrados como perda junto com esse destino.

**Econômica.** Consumir primeiro o lote mais antigo reduz as perdas por vencimento. O aviso de vencimento próximo permite usar o lote antes que vença. O alerta de estoque mínimo evita falta de medicamentos, e o ajuste de inventário corrige diferenças entre o sistema e a contagem física.

**Social.** Casos de emergência, como atropelamento e intoxicação, passam à frente na espera, respeitando a ordem de chegada entre si.

## 8. Desenvolvimento incremental

Domingo, 22/11/2026. Criação do repositório e do README inicial com a concepção do projeto.

Segunda-feira, 23/11/2026. Módulo 1, classe `No`. Módulo 2, `ListaEncadeada` em duas etapas, primeiro inserção e exibição, depois remoção. Módulo 3, `Fila`. Módulo 4, controle de atendimento com filas de emergência e normal e consultórios. Módulo 5, cadastro de tutores e animais.

Terça-feira, 24/11/2026. Módulo 6, árvore N-ária de sistemas do animal. Módulo 7, estoque com lista de produtos e fila de lotes, descarte de vencidos, ajuste de inventário e alertas. Módulo 8, pilha e prontuário. Módulos 9 e 10, pagamento, baixa no estoque e controle do consumo. Módulo 11, simulação do atendimento completo. Versão final deste README.
