import string
import random

LETTERS = string.ascii_letters
NUMMERS = string.digits
PUNCTUATIE = string.punctuation 

def get_password_length():
    Lengte = input("Hoe lang moet je wachtwoord zijn?: ")
    return int(Lengte)

def password_generator(Lengte = 8):
    KeuzeLijst = f'{LETTERS}{NUMMERS}{PUNCTUATIE}'

    KeuzeLijst = list(KeuzeLijst)
    random.shuffle(KeuzeLijst)

    random_wachtwoord = random.choices(KeuzeLijst, k=Lengte)
    random_wachtwoord = ''.join(random_wachtwoord)
    return random_wachtwoord

password_one = password_generator()
password_length = get_password_length()
WachtwoordLengte = password_generator(password_length)

print("Je Wachtwoord (Lengte van " + str(len(WachtwoordLengte)) + "):\t\t" + WachtwoordLengte)