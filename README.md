# Simulação de Máquina de Turing

## Descrição do Projeto

Este projeto simula uma Máquina de Turing, baseada em uma definição de estados e transições para processar diferentes cadeias de entrada. A Máquina de Turing é configurada para alterar o conteúdo de sua fita e movimentar o cabeçote conforme as regras de transição definidas, buscando alcançar um estado final ou finalizar quando as entradas são processadas.

## Estrutura do Projeto

O projeto inclui três arquivos principais:

1. **arquivo.json**: Contém a definição da Máquina de Turing.
   - **initial**: Estado inicial (0).
   - **final_state**: Estado final (4).
   - **blank_symbol**: Símbolo de espaço em branco `_` na fita.
   - **tape**: Representação inicial da fita.
   - **transitions**: Conjunto de transições no formato `{from, to, read, write, move}`, especificando como a máquina se comporta para cada símbolo lido.

2. **entrada (1).txt**: Conjunto de cadeias de entrada para a Máquina de Turing processar, com exemplos como `aabb`, `aaaaaaaaa`, `bbbbbbbbb`, `aaaabbbb`, `abab`.

3. **Turing_Machine.py**: Código Python que implementa a lógica da Máquina de Turing. Este script lê as definições do arquivo JSON e processa cada cadeia do arquivo de entrada, aplicando as transições e movendo o cabeçote na fita.

## Execução do Projeto

1. **Configuração**: Certifique-se de que todos os arquivos estão na mesma pasta.
2. **Execução**: Execute `Turing_Machine.py` em um ambiente Python com o comando:
   ```bash
   python Turing_Machine.py
