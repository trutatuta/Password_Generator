'''
Password Generator
'''
import random
import string


class Password:
    '''Class Password'''
    password = ''

    def __init__(self, length, options):
        self.length = length
        self.options = options

    def generate_password(self):
        '''Password generation'''
        for _ in range(self.length):
            opt = random.choice(list(self.options.keys()))
            if opt == 'upper':
                self.password += random.choice(string.ascii_uppercase)
                self.options[opt] -= 1
                if self.options[opt] == 0:
                    del self.options[opt]
            if opt == 'lower':
                self.password += random.choice(string.ascii_lowercase)
                self.options[opt] -= 1
                if self.options[opt] == 0:
                    del self.options[opt]
            if opt == 'digits':
                self.password += random.choice(string.digits)
                self.options[opt] -= 1
                if self.options[opt] == 0:
                    del self.options[opt]
            if opt == 'punctuation':
                self.password += random.choice(string.punctuation)
                self.options[opt] -= 1
                if self.options[opt] == 0:
                    del self.options[opt]

    def show_password(self):
        '''Password is ready to use'''
        print("Your password: " + self.password)

option = {}
leng = int(input("Enter a length: "))
upper = int(input("Enter the number of uppercase letter: "))
if upper > 0:
    option['upper'] = upper

lower = int(input("Enter the number of lowercase letter: "))
if lower > 0:
    option['lower'] = lower

digits = int(input("Enter the number of digits: "))
if digits > 0:
    option['digits'] = digits

punctuation = int(input("Enter the number of punctuation: "))
if punctuation > 0:
    option['punctuation'] = punctuation

if upper + lower + digits + punctuation == leng:
    ps = Password(leng, option)

    ps.generate_password()

    ps.show_password()
else:
    print("ERROR")
