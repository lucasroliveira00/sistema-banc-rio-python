# Sistema Bancário Simples

Este código em Python simula um sistema bancário com funcionalidades básicas, como depósito, saque e exibição de extrato. O usuário interage com o sistema por meio de um menu, onde pode escolher as opções disponíveis.

## Funcionalidades

1. **Depósito**: Permite ao usuário adicionar um valor ao saldo da conta.
2. **Saque**: Permite ao usuário retirar um valor do saldo da conta, respeitando o limite diário e o valor disponível.
3. **Extrato**: Exibe todas as movimentações (depósitos e saques) realizadas até o momento, bem como o saldo atual.
4. **Sair**: Encerra o sistema bancário.

## Variáveis Principais

- `saldo`: Armazena o saldo atual da conta bancária.
- `limite`: Define o limite máximo para cada saque (R$ 500,00).
- `numero_saques`: Controla o número de saques feitos no dia.
- `LIMITE_SAQUES`: Limita o número de saques diários (máximo de 3).
- `log_movimentacoes`: Lista que registra o histórico de movimentações (depósitos e saques).

## Funções

### 1. `depositar(valor_deposito)`
- **Parâmetro**: `valor_deposito` (float) – Valor a ser depositado na conta.
- **Descrição**: Verifica se o valor do depósito é válido (maior ou igual a 0) e, caso seja, adiciona ao saldo. Também registra o depósito no histórico de movimentações.
- **Exemplo**:
    ```python
    depositar(100)  # Adiciona R$ 100 ao saldo
    ```

### 2. `sacar(valor_saque)`
- **Parâmetro**: `valor_saque` (float) – Valor que o usuário deseja sacar.
- **Descrição**: Permite o saque se o valor estiver dentro dos limites diários e não for superior ao saldo disponível. Também registra o saque no histórico de movimentações.
- **Regras**:
  - O valor do saque deve ser maior que 0.
  - Não pode ultrapassar o saldo disponível.
  - Não pode ultrapassar o limite de R$ 500,00 por saque.
  - O número de saques diários é limitado a 3.
- **Exemplo**:
    ```python
    sacar(200)  # Retira R$ 200 do saldo se as condições forem atendidas
    ```

### 3. `exibir_extrato()`
- **Descrição**: Exibe o histórico de depósitos e saques realizados, junto com o saldo atual da conta.
- **Exemplo**:
    ```python
    exibir_extrato()  # Mostra todas as transações e o saldo atual
    ```

## Fluxo de Execução

O código principal utiliza um loop `while True` para exibir um menu interativo até que o usuário escolha a opção de sair (`[0] Sair`).

- **Menu**:
    ```text
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    ```

Dependendo da escolha do usuário, o programa chama uma das funções:
- `[1]` para depósito
- `[2]` para saque
- `[3]` para exibir o extrato
- `[0]` para encerrar o sistema

## Considerações

- O sistema controla o número de saques permitidos por dia (máximo de 3).
- Cada saque é limitado a R$ 500,00.
- O extrato exibe todas as transações realizadas.
- Há tratamento para que não seja possível digitar valores negativos no saque e depósito.
