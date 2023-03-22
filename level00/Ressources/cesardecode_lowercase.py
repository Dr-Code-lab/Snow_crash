import string
import time

class CesarDecoder:
    # def __init__(self):
    #     self.line = line

    def DecodeThis(line):
        
        
        _alphabet = list(string.ascii_lowercase)
        _numbers = list(range(1,27))

        letters = dict(

            zip(

                _numbers,

                _alphabet,

            )

        )

        id_letters = dict(

            zip(

                _alphabet,

                _numbers,

            )

        )

        pwd = line
        tmp = pwd

        for steps in range(1, 27):

            for index in range(0, len(pwd)):

                id = id_letters.get(pwd[index])
                if id is not None :
                    if id + steps <= 26:

                        pwd = pwd[0:index] + letters.get(id + steps) + pwd[index + 1 : len(pwd)]

                    else:

                        pwd = pwd[0:index] + letters.get(id + steps - 26) + pwd[index + 1 : len(pwd)]

            print('\033[96m', pwd, '\033[0m')

            pwd = tmp