import string
import random


def randomcode():
    code = ''
    letter = string.ascii_letters+string.digits
    for i in range(5):
        code = code+str(random.choice(letter))
    return code