import re
import shutil
import tempfile

temp_dirs = []


def make_temp_dir(prefix=''):
    global temp_dirs
    directory = tempfile.mkdtemp(prefix=prefix)
    temp_dirs.append(directory)
    return directory


def remove_temp_dirs():
    global temp_dirs
    for directory in temp_dirs:
        shutil.rmtree(directory, ignore_errors=True)


# def extract_number(cur_line):
#     firstCom = cur_line.find("'")
#     secondCom = cur_line.find("'", firstCom + 1)
#     levelStr = cur_line[firstCom + 1: secondCom]
#     return int(levelStr)

def extract_number(cur_line):
    """Extrai o primeiro número inteiro de uma string.

    Args:
        string: A string de entrada.

    Returns:
        O número inteiro extraído, ou None se nenhum número for encontrado.
    """

    # Padrão para encontrar um ou mais dígitos
    padrao = r'\d+'
    resultado = re.search(padrao, cur_line)

    if resultado:
        return int(resultado.group())
    else:
        return -1


def extract_target_api(yml_path):
    print("extract_target_api = {}".format(yml_path))
    with open(yml_path, 'r') as fd:
        for line in fd.readlines():
            print("line={}".format(line))
            if 'targetSdkVersion' in line:
                print("********************* targetSdkVersion = {}".format(extract_number(line)))
                # return 29
                return extract_number(line)
    return -1
