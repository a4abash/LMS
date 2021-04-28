import string
import random


def getRandomPassword():
    password = ''
    letter = string.ascii_letters+string.digits+string.punctuation

    for i in range(10):
        password = password+str(random.choice(letter))
    return password