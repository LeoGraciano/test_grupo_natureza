from apps.exceptions.integer import print_exception_integer

def max_product(array: list()) -> int:
    max_array = []
    condition_max = 3
    result = 0

    while len(array) > 0 and len(max_array) < condition_max:
        if max(array) == 0:
            break

        max_array.append(max(array))
        array.remove(max(array))
    

    for i, number in enumerate(max_array):
        if i == 0:
            result = number
            continue

        result *= number

    return  result

def option_max_product():
    array_start = []
    count = 1
    while True:
        print('\nDigite 0 para parar a contagem')
        try:
            number = int(input(f'Digite {count}° número inteiro: \n'))

            if number == 0:
                break

            array_start.append(number)
            count += 1

        except ValueError:
            print_exception_integer()

    print('Lista: ' + str(array_start))
    return max_product(array_start)