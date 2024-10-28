# Calculadora com Menu de Operações e Loop Infinito

Este projeto foi desenvolvido como parte do curso de Introdução à Programação oferecido pela Proz em parceria com a AWS no programa Talento Cloud. Ele implementa uma calculadora que permite ao usuário realizar operações matemáticas básicas continuamente até que a opção de sair seja escolhida. O exercício reforça o uso de funções, laços de repetição e estruturas condicionais em Python.

## Funcionalidade do Programa

O código exibe um menu com as opções de operações e permite ao usuário realizar operações matemáticas até que ele decida sair. Após cada operação, o menu é exibido novamente, permitindo a escolha de uma nova operação. As operações possíveis são:

1. **Soma**
2. **Subtração**
3. **Multiplicação**
4. **Divisão**
5. **Sair** (opção 0)

Caso o usuário insira uma opção inválida, uma mensagem de erro é exibida, e o menu é reapresentado.

### Estrutura do Código

1. **Função `calculadora()`**
   - Um loop infinito (`while True`) mantém o programa em execução até que a opção de sair seja escolhida.
   - O menu de operações é exibido a cada ciclo, pedindo que o usuário escolha uma opção.
   
2. **Opções do Menu**
   - Se o usuário digitar `0`, o programa exibe uma mensagem de encerramento e termina.
   - Se a entrada for `1`, `2`, `3` ou `4`, o usuário insere dois números para realizar a operação correspondente:
     - **Opção 1**: Soma
     - **Opção 2**: Subtração
     - **Opção 3**: Multiplicação
     - **Opção 4**: Divisão (com verificação para evitar divisão por zero)
   - Qualquer outra entrada exibe a mensagem "Essa opção não existe" e retorna ao menu.
   
3. **Exibição de Resultado**
   - O resultado é exibido formatado com duas casas decimais.
   - Após a exibição, o menu reaparece para uma nova operação.

## Exemplo de Uso

### Menu Inicial
```plaintext
Escolha uma das opções:
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
0- Sair
Digite a operação: 1
```

### Exemplo de Operação
```plaintext
Digite um número: 10
Digite outro número: 5
O resultado de 10.0 + 5.0 é: 15.00.
```

### Mensagem para Opção Inválida
```plaintext
Essa opção não existe.
```

## Tecnologias e Conceitos Utilizados

- **Python**: Linguagem de programação.
- **Funções**: Definição e chamada de função `calculadora()`.
- **Loop Infinito**: `while True` para repetição contínua até a opção de saída.
- **Estrutura Condicional**: `if-elif-else` para o menu de opções e operações.
- **Verificação de Erro**: Tratamento de divisão por zero e opções inválidas.

## Autor

Caio Frederico, como parte do curso Talento Cloud da Proz e AWS.
