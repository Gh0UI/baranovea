"""Бесконечное передвижение персонажа, возвращает координаты"""
xy=[0,0]
move= 5

while (True): 
    move= int(input ('куда пойти персонажу?\n 1-вверх\n 2-вниз\n 3-влево\n 4-вправо\n 0-выход\n'))
    if move==0: break
    if move not in range(5): 
        print('некорректный ввод') 
        continue

    step= int(input ('сколько сделать шагов?\n'))

if move==1:
    """движение вверх"""
    xy[1] =xy[1] + step

elif move==2:
    """движение вниз"""
    xy[1] =xy[1] - step

elif move==3:
    """движение влево"""
    xy[0] =xy[0] - step

elif move==4:
    """движение вправо"""
    xy[0] =xy[0] + step

    print("\t",list(xy),'\n')
