"""Передвижение персонажа, возвращает координаты"""
xy=[0,0]
move= int(input ('куда пойти персонажу?\n 1-вверх\n 2-вниз\n 3-влево\n 4-вправо\n'))

while (move ==0 or move > 4): 
    move= int(input ('введите корректное число\n'))


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

print(list(xy))