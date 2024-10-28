# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
# Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

# Criando a função da calculadora
def calculadora():
    # Enquanto for True
    while True:
        # Crie a interface de escolha
        print('\nEscolha uma das opções: ');
        print('1- Soma');
        print('2- Subtração');
        print('3- Multiplicação');
        print('4- Divisão');
        print('0- Sair');

        # Pegando a escolha do usuário
        opcao = input('Digite a operação: ');

        # Condições para cara operação
        if opcao == '0':
            print('Encerrando calculadora.');
            break;
    
        elif opcao in ['1', '2', '3', '4']:
            # Solicitando os números ao usuário
            num1 = float(input('Digite um número: '));
            num2 = float(input('Digite outro número: '));

            # Calculando
            if opcao == '1':
                resultado = num1 + num2;
                print(f'O resultado de {num1} + {num2} é: {resultado:.2f}.');
        
            elif opcao == '2':
                resultado = num1 - num2;
                print(f'O resultado de {num1} - {num2} é: {resultado:.2f}.');
        
            elif opcao == '3':
                resultado = num1 * num2;
                print(f'O resultado de {num1} * {num2} é: {resultado:.2f}.');
        
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2;
                    print(f'O resultado de {num1} / {num2} é: {resultado:.2f}.');
                else:
                    print('Erro, você não pode dividir um número por 0.')
        else:
            print('Essa opção não existe.')

# Chamando a função calculadora
calculadora();