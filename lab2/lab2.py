"""
Лабораторная работа №2
Вариант 4
"""


def decoder(byte_string):
    """
    Return decoded string from byte string(support utf-8,uft-16,utf-32)
    :param byte_string: byte string encoded with utf codec
    :return: utf-8 string
    """
    CODECS = ('utf-32', 'utf-8', 'utf-16')
    for codec in CODECS:
        try:
            byte_string.decode(codec)
        except UnicodeDecodeError:
            pass
        else:
            return byte_string.decode(codec)


students = ['Арабаджи', 'Шарапов', 'Баранов', 'Цынтел', 'Талпа', 'Жеков']

with open(r"C:\Users\jekov\Desktop\lb2.txt",mode='w',encoding='utf-8') as file:
    for student in students:
        student += '\n'
        file.write(student)
    file.write('\n')

f = "Жеков".encode('utf-16')
i = "Максим".encode('utf-32')
o = "Николаевич".encode('cp1251').decode('cp1251').encode('utf-8')

fio = '\n'.join([decoder(item) for item in (f, i, o)])

with open(r"C:\Users\jekov\Desktop\lb2.txt", 'ab') as file:
    file.write(fio.encode('cp1251'))

