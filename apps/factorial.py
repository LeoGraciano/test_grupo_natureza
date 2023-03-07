from apps.exceptions.integer import print_exception_integer


def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n - 1)
    return 1

def option_factorial():
    while True:
        try:
            value = int(input('Digite um número inteiro: \n'))
            break
        except ValueError:
            print_exception_integer()

    return factorial(value)
