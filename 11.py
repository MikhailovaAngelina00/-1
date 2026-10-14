import time
import random
RESET = '\u001b[0m'
def squ():
    height = 4
    pixel = ' '
    length = 11
    offsets = [1,3,5,8,10,2]
    colors = [196, 202, 220,28,27,91]
    offset = offsets[0]

    while True:
        for color in colors:
            for line in range(height):
                 print(f'{pixel * offset}\u001b[48;5;{color}m{pixel * length}{RESET}')


            print(f'\u001b[{height}A')
            length = 11
            offset = random.choice(offsets)
            time.sleep(0.3)

squ()