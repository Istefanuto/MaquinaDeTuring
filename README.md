Simulação de Máquina de Turing
Descrição do Projeto
Este projeto simula uma Máquina de Turing, baseada em uma definição de estados e transições para processar diferentes cadeias de entrada. A Máquina de Turing é configurada para alterar o conteúdo de sua fita e movimentar o cabeçote conforme as regras de transição definidas, buscando alcançar um estado final ou finalizar quando as entradas são processadas.

Estrutura do Projeto
O projeto inclui três arquivos principais:

arquivo.json: Contém a definição da Máquina de Turing.

initial: Estado inicial (0).
final_state: Estado final (4).
blank_symbol: Símbolo de espaço em branco _ na fita.
tape: Representação inicial da fita.
transitions: Conjunto de transições no formato {from, to, read, write, move}, especificando como a máquina se comporta para cada símbolo lido.
entrada (1).txt: Conjunto de cadeias de entrada para a Máquina de Turing processar, com exemplos como aabb, aaaaaaa, bbbbbbb, aaaabbbb, abab.

Turing_Machine.py: Código Python que implementa a lógica da Máquina de Turing. Este script lê as definições do arquivo JSON e processa cada cadeia do arquivo de entrada, aplicando as transições e movendo o cabeçote na fita.

Execução do Projeto
Configuração: Certifique-se de que todos os arquivos estão na mesma pasta.
Execução: Execute Turing_Machine.py em um ambiente Python com o comando:
bash
Copiar código
python Turing_Machine.py
Resultados: O programa irá mostrar o processamento de cada cadeia de entrada e o estado final da fita após a execução das transições definidas.
Funcionamento da Máquina
A Máquina de Turing funciona com as seguintes transições, definidas no arquivo JSON:

from: Estado atual.
to: Próximo estado.
read: Símbolo a ser lido na fita.
write: Símbolo a ser escrito na fita.
move: Direção do movimento do cabeçote (R para direita, L para esquerda).
Exemplo de Transição
Para a entrada aabb, a máquina segue a lógica de transições, alterando os caracteres e movendo o cabeçote até atingir o estado final ou até processar todos os caracteres da fita.

Observações
A fita é dinâmica e cresce conforme necessário.
O projeto requer Python 3.6 ou superior.
As cadeias de entrada podem ser ajustadas conforme necessário no arquivo entrada (1).txt.
