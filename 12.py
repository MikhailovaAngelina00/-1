black = '\u001b[40m'
white='\u001b[47m'
reset = '\u001b[0m'
pixel = ' '
height = 6
for i in range(height):
    if i<1:
        print(f'{white}{pixel*5}{black}{pixel*7}{white}{pixel*7}{black}{pixel*7}{white}{pixel*5}{reset}')
    elif i<2:
        print(f'{white}{pixel * 2}{black}{pixel * 3}{white}{pixel * 7}{black}{pixel*3}{white}{pixel * 1}{black}{pixel * 3}{white}{pixel * 7}{black}{pixel * 3}{white}{pixel * 2}{reset}')
    elif i<3:
        print(
            f'{white}{pixel * 1}{black}{pixel * 3}{white}{pixel * 9}{black}{pixel * 2}{black}{pixel * 3}{white}{pixel * 9}{black}{pixel * 3}{white}{pixel * 1}{reset}')
    elif i<4:
        print(
            f'{white}{pixel * 2}{black}{pixel * 3}{white}{pixel * 7}{black}{pixel * 3}{white}{pixel * 1}{black}{pixel * 3}{white}{pixel * 7}{black}{pixel * 3}{white}{pixel * 2}{reset}')
    elif i<5:
        print(f'{white}{pixel * 5}{black}{pixel * 7}{white}{pixel * 7}{black}{pixel * 7}{white}{pixel * 5}{reset}')


