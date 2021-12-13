first_operand= float (input ('введите первое число: '))
second_operand= float (input ('введите второе число: '))

addition=(first_operand
          +second_operand)
"""сложение  чисел"""

subtraction=(first_operand
             -second_operand)
"""разность  чисел"""

multiplication=(first_operand
                *second_operand)
"""произведение  чисел"""

division=(first_operand
          /second_operand)
"""частное чисел"""

power=(first_operand
       **second_operand)
"""степень чисел"""

mod_division=(first_operand
              %second_operand)
"""частное по модулю"""

int_division=(first_operand
              //second_operand)
"""целое частного"""


print(' сумма числел: \t',addition,'\n','разность числел: \t', subtraction,'\n','произведение числел: \t', multiplication,'\n',
 'частное числел: \t', division,'\n', 'степень числел: \t', power,'\n', 'частное по модулю: \t', mod_division,'\n', 'целое частного: \t', int_division)