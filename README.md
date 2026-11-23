markdown

\# Projeto Clínica Veterinária



Disciplina Estrutura de Dados, Fatec Rio Claro. Prof. Orlando.



\## 1. Concepção do projeto



Este projeto desenvolve, em Python, um mini sistema de gestão para uma clínica veterinária. Ele segue o mesmo raciocínio do projeto anterior da disciplina, a Oficina Mecânica Sustentável, aplicado a um novo contexto. Onde a oficina atendia veículos, a clínica atende animais. Onde a oficina tinha boxes, a clínica tem consultórios.



O sistema gerencia o ciclo completo de um atendimento. O animal chega e entra na espera, com prioridade para emergências. Quando um consultório fica livre, o próximo animal é chamado e o prontuário é aberto. O veterinário faz o diagnóstico numa árvore de sistemas do animal, marcando os itens alterados. Medicamentos e procedimentos entram no prontuário ao longo do atendimento. Após a alta, o prontuário é fechado, o estoque é baixado pelo lote mais antigo, o pagamento é registrado e o sistema anota o que cada animal consumiu.



Todas as estruturas de dados serão implementadas em classes próprias, separadas das regras da clínica. Não usaremos list nem dict do Python para guardar os dados do problema.



\## 2. Estruturas planejadas



\- Lista encadeada, fila, pilha e árvore N-ária, em classes próprias.

\- Combinações de estruturas:

&#x20; - Fila + Fila: atendimento com prioridade para emergências.

&#x20; - Lista de tutores, cada um com uma Lista de animais.

&#x20; - Lista de produtos, cada um com uma Fila de lotes.



O detalhamento das classes, dos métodos e das justificativas será acrescentado conforme os módulos forem concluídos.



\## 3. Sustentabilidade



O descarte de materiais cirúrgicos, perfurocortantes e medicamentos vencidos seguirá as normas vigentes para resíduos de serviços de saúde.



