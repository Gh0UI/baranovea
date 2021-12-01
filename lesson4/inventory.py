import re
from typing import Dict
stick= {'палка':1 }
stone= {'камень':2 }
dirt= {'земля':3 }

inventory=[]
weight=0
max_weight=10

while (True): 
    print(f'{inventory} \tвес:{weight}')
    choise= int(input ('1-добавить предметы в инвентарь\n2-удалить предметы из инвентаря\n3-выход\n'))
    if choise==3: break
     
    if choise==1: 
        
        choise_item= int(input ('1-палка\n2-камень\n3-земля\n'))
        if choise_item==1 and ((weight+stick.get('палка')<=max_weight)):
            inventory.append(stick)
            weight=weight+stick.get('палка')
        elif choise_item==2 and ((weight+stone.get('камень')<=max_weight)):
            inventory.append(stone)
            weight=weight+stone.get('камень')
        elif choise_item==3 and ((weight+dirt.get('земля')<=max_weight)):    
            inventory.append(dirt)
            weight=weight+dirt.get('земля')
        elif choise_item not in range(4):
            print('некорректный ввод') 
            continue    
        else:
            print('превышен лимит') 
            continue  

    elif choise==2:       
         choise_del= int(input ('какой номер предмет удалить?\n'))
         choise_del=choise_del-1
         if choise_del >= (len(inventory)):
             print('введено неверное значение')
             continue
          #преобразование словаря в строку  
         weight_del=str(inventory[choise_del])
         #выборка числа из строки   
         for c in weight_del:
             if c.isdigit():num=c
         #вычитание веса и очистка элемента
         weight=weight-int(num)
         inventory.pop(choise_del)
    else:
          print('некорректный ввод')  
          continue 
        
         
            