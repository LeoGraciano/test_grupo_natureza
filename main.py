from apps.palindrome import option_palindrome
from apps.factorial import option_factorial
from apps.max_product import option_max_product


def call(option: int) -> any:
    if option == 1:
        return option_palindrome()
    elif option == 2:
        return option_factorial()
    elif option == 3:
        return option_max_product()


def options() -> None:
    print(50*'#')
    print('1 - Verifica uma palavra é Palindrome.')
    print('2 - Qual fatorial de terminando número inteiro.')
    print('3 - Maior produto de até 3 números de uma lista')
    print('\n')

if __name__ == '__main__':
    options()
    op = int(input('Qual sistema deixa utilizar ?\n'))
    result = call(op)
    print(f'Resultado: {result}')