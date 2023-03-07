def is_palindrome(string: str) -> bool:
    return string.lower() == (string[::-1]).lower()


def option_palindrome():
    word = input('Digite uma palavra: \n')
    return is_palindrome(word)
