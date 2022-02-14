import pathlib
import os
import glob
import unicodedata


'''
https://docs.python.org/3/library/pathlib.html
'''

# print(os.name)  # Posisx - Linux e Mac  # nt - Windows

'''
Sistemas de arquivos
regex

'''

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def stander(path, dryrun=True):
    new_path = pathlib.Path(path) / '*'
    for files in glob.glob(str(new_path)):
        file_old_name = pathlib.Path(files)
        file_name = file_old_name.stem.lower()
        file_stem = pathlib.Path(files).suffixes
        if file_name.find('__') != -1 or not file_stem:
            continue
        file_name = file_name.replace('  ', ' ')\
        .replace(',', ' ').replace(' ', '_').replace('__', '_')
        file_name = strip_accents(file_name)
        file_name = new_path.parent/pathlib.Path(str(file_name) + file_stem[-1])
        print(file_name)

        if not dryrun:
            os.rename(files, file_name)
            print(file_name)




stander('C:\\Users\\Miguel\\Envs\\ProjetosPyMarina', False)





'''
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
'''

'''
Todos os nomes com letras minusculas
Retirar virgulas
retirar underlines em excessso
Espaços substituidos por underline "_"
Sem acentos e sem "ç"

'''