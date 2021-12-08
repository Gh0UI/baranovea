list=[]
encode_list=[]
decode_list=[]
print("Введите строку:\nдля выхода наберрите 'выход'\n")
num=1
while num!=0:
        try:
            string =(input())
            if string=='выход': break
            list.append(string)
        except ValueError:
            print("Вы ввели не строку. Повторите ввод")

def f_encode(list):
    i=0
    sum=0
    encode_list=[]
    while i < len(list):       
        encode_list.insert(i,list[i].encode('utf-8'))
        i += 1
    return encode_list

encode_list=f_encode(list)

print('закодированные строки\n')
for elem in encode_list:
    print(elem)

def f_decode(list):
    i=0
    decode_list=[]
    while i < len(list):       
        decode_list.insert(i,list[i].decode('utf-8'))
        i += 1
    return decode_list

decode_list=f_decode(encode_list)

print('раскодированные строки\n')

for elem in decode_list:
    print(elem)