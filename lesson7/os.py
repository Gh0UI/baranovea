import os
print(f' имя ОС:\t\t{os.name}\n'
      f' имя пользователя:\t{os.getlogin()}\n'
      f' файлы в директории:\t{os.listdir(path=".")}')