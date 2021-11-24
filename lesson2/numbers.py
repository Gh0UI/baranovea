first_operand= float (input ('введите первое число: '))
second_operand= float (input ('введите второе число: '))
addition=first_operand+second_operand
subtraction=first_operand-second_operand
multiplication=first_operand*second_operand
division=first_operand/second_operand
power=first_operand**second_operand
mod_division=first_operand%second_operand
int_division=first_operand//second_operand

print(' сумма числел: \t',addition,'\n','разность числел: \t', subtraction,'\n','произведение числел: \t', multiplication,'\n',
 'частное числел: \t', division,'\n', 'степень числел: \t', power,'\n', 'частное по модулю: \t', mod_division,'\n', 'целое частного: \t', int_division)