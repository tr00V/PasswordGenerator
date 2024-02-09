from random import choice


class Password:
    chars_letters_lower = 'abcdefghijklnopqrstuvwxyz'
    chars_letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_numbers = '1234567890'
    chars_symbols = '+-/*!&$#?=@<>'

    def __init__(self, length: int = 12, numbers: bool = True, letters_lower: bool = True, letters_upper: bool = True,
                 symbols: bool = True):
        self.length = length
        self.numbers = numbers
        self.letters_lower = letters_lower
        self.letters_upper = letters_upper
        self.symbols = symbols
        self.chars = self._create_chars()

    def __repr__(self):
        return "Password"

    def _create_chars(self) -> str:
        chars = ''
        if self.numbers:
            chars += self.chars_numbers
        if self.letters_upper:
            chars += self.chars_letters_upper
        if self.letters_lower:
            chars += self.chars_letters_lower
        if self.symbols:
            chars += self.chars_symbols
        return chars

    def generate(self) -> str:
        password = ''
        for i in range(self.length):
            password += choice(self.chars)
        return password

    def returns_passwords(self) -> list:
        passwords = list()
        for i in range(10):
            passwords.append(self.generate())
        return passwords

    @staticmethod
    def __check_symbols_int_text(symbols: list, text: str) -> bool:
        for symbol in symbols:
            if symbol in text:
                return True
        return False

    def _check_valid(self, password: str) -> dict[str, list[bool, str]]:
        if len(password) >= 12:
            if self.__check_symbols_int_text(list(self.chars_letters_lower), password):
                if self.__check_symbols_int_text(list(self.chars_letters_upper), password):
                    if self.__check_symbols_int_text(list(self.chars_numbers), password):
                        if self.__check_symbols_int_text(list(self.chars_symbols), password):
                            return {password: [True, '']}
                        else:
                            recommendation = 'Нет специальных символов'
                            return {password: [False, recommendation]}
                    else:
                        recommendation = 'Нет цифр'
                        return {password: [False, recommendation]}
                else:
                    recommendation = 'Нет заглавных букв'
                    return {password: [False, recommendation]}
            else:
                recommendation = 'Нет строчных букв'
                return {password: [False, recommendation]}
        else:
            recommendation = 'Слишком короткий'
            return {password: [False, recommendation]}

    def check_passwords(self) -> dict:
        checked_passwords = {}

        passwords = self.returns_passwords()
        for password in passwords:
            checked_password = self._check_valid(password)
            checked_passwords[password] = checked_password[password]

        return checked_passwords
