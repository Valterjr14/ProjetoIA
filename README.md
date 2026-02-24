## Planejamento de Rotas para Drone com Custo Energético Variável em Ambientes com Restrições

1.Introdução
    Este trabalho propõe o desenvolvimento de um agente inteligente capaz de planejar rotas para um drone em um ambiente discreto representado por um grid. O ambiente inclui obstáculos que não podem ser atravessados e regiões com vento, que aumentam o custo de movimentação do agente. Dessa forma, o problema consiste em encontrar um caminho até o destino que minimize o custo energético total, e não apenas o número de movimentos.

2.Especificação Formal do Problema

    2.1. Representação dos Estados
        Cada estado representa a posição atual do drone no ambiente, modelado como um grid bidimensional:
        estado = (x, y)
        Onde:
        x representa a linha
        y representa a coluna

    2.2. Estado Inicial
        O estado inicial corresponde à posição de partida do drone:
        initial = (x_inicial, y_inicial)
        Exemplo:
        initial = (0, 0)

    2.3 Estado Objetivo
        O estado objetivo corresponde à posição de destino da entrega:
        goal = (x_goal, y_goal)
        Exemplo:
        goal = (3, 4)
        O teste de objetivo é definido como:
        goal_test(s) = True, se s == goal

    2.4 Ações 
        As ações representam os movimentos possíveis do drone no ambiente:
        A = {UP, DOWN, LEFT, RIGHT}
        As ações são válidas apenas quando:
        - não ultrapassam os limites do grid
        - não levam a células com obstáculos

    2.5 Modelo de Transição
        A função de transição define o novo estado após a execução de uma ação:
        result((x, y), UP) = (x-1, y)
        result((x, y), DOWN) = (x+1, y)
        result((x, y), LEFT) = (x, y-1)
        result((x, y), RIGHT) = (x, y+1)
        Desde que a ação seja válida.

    2.6 Função de Custo
        O custo de caminho é definido com base no tipo de célula do ambiente:
        - célula livre (.): custo = 1
        - célula com vento (W): custo = 3
        - célula com obstáculo (X): não é permitida
        Assim, o custo total de um caminho é dado por:
        path_cost = soma dos custos das células percorridas
        Esse custo representa o consumo energético do drone ao longo do trajeto.

    2.7 Heurística (h(n))
        Para a aplicação do algoritmo A*, é utilizada uma função heurística baseada na distância de Manhattan:
        h(n) = |x - x_goal| + |y - y_goal|
        Essa heurística estima o custo mínimo restante até o objetivo.

    2.8 Observações
        O problema difere de abordagens tradicionais de menor caminho ao considerar custos variáveis no ambiente, tornando a solução dependente não apenas da distância, mas também das condições do trajeto. Dessa forma, o agente é capaz de tomar decisões mais eficientes do ponto de vista energético.

3. Classificação do Ambiente

    3.1 Observabilidade
        O ambiente é totalmente observável, pois o agente possui acesso completo à representação do grid, incluindo a localização de obstáculos, regiões com vento e o destino. Dessa forma, não há incerteza sobre o estado atual do ambiente.

    3.2 Determinismo
        O ambiente é determinístico, uma vez que a execução de uma ação em um determinado estado sempre resulta no mesmo estado seguinte. Por exemplo, ao executar a ação de movimento para cima (UP), o agente sempre se desloca para a mesma posição, desde que a ação seja válida.

    3.3 Episódico vs. Sequencial
        O ambiente é sequencial, pois cada ação executada pelo agente influencia diretamente os estados futuros. As decisões tomadas em um determinado momento impactam o custo total do caminho até o objetivo.

    3.4 Estático vs. Dinâmico
        O ambiente é considerado estático, pois não sofre alterações durante a execução do agente. As posições dos obstáculos e das regiões com vento permanecem constantes ao longo do tempo.

    3.5 Discreto vs. Contínuo
        O ambiente é discreto, uma vez que:
        - os estados são representados por posições em um grid finito
        - as ações são finitas e bem definidas
        - o tempo evolui em etapas discretas

    3.6 Número de Agentes
        O ambiente é de agente único, pois há apenas um agente (o drone) atuando no sistema, sem interação com outros agentes.

4. Arquitetura e Algoritmos
    O projeto respeita a separação Ambiente - Agente - Programa de Agente:
    -   Ambiente (env/grid_env.py): Mantém o estado do grid e renderiza o drone.
    -   Programa de Agente (agents/drone_agent.py): Utiliza a classe SimpleProblemSolvingAgentProgram do AIMA para formular o problema e    gerar um plano.
    -   Algoritmo de Busca: Foi utilizado o *A (A-Estrela)** com a Heurística de Manhattan.
        -   Justificativa: O A* é ótimo e completo. A distância de Manhattan é admissível para movimentos em grid 4-conexo, garantindo o caminho de menor custo energético.

5. Instruções de Execução
    
    Pré-requisitos:
        Python 3.10 ou superior.
        Não é necessário instalar bibliotecas externas (o projeto usa unittest nativo).
        Os arquivos search.py e utils.py devem estar na raiz do projeto (já incluídos neste repositório).
        
    Como Rodar a Simulação:
    Abra o terminal ou PowerShell na pasta raiz do projeto e utilize o comando correspondente ao seu sistema:
        Windows (PowerShell ou CMD):
            python main.py
        Linux / macOS:
            python3 main.py
        
        Pressione Enter no terminal para avançar cada passo do drone.

    Como Rodar os Testes Automatizados:
    Para verificar a lógica de custos e obstáculos:
        Windows:
            python tests/test_drone.py
        Linux / macOS:
            python3 tests/test_drone.py

6. Estrutura do Projeto
    O projeto segue a organização mínima exigida:
    -   /agents: Lógica de decisão do drone.
    -   /env: Classe de ambiente e método render().
    -   /problems: Definição da classe DroneProblem.
    -   /tests: Testes unitários de custo e colisão.
    -   main.py: Ponto de entrada do sistema.