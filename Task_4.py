# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_rle(txt): # шифрование строки
    encoding = ''
    i = 0
    while i < len(txt): # цикл подсчета количества вхождений символа с индексом i
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + txt[i] # добавляем в строку символ и количество его вхождений
        i += 1
    return encoding


def decode_rle(data): # расшифровка строки
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():    # если символ - число
            count += char
        else:                # если не число, добавляем в строку
            decoding += char * int(count)
            count = ''
    return decoding


def read_data(file): # получение данных из файла
    with open(str(file), 'r', encoding="UTF-8") as data:
        input_string = data.read()
    return input_string


input_text = "C:\\Users\\Надюша\\Desktop\\Python_Homework5\\input_text.txt" # исходный текст
tx = "C:\\Users\\Надюша\\Desktop\\Python_Homework5\\encoded_input_text.txt" # сжатый текст
text1 = "C:\\Users\\Надюша\\Desktop\\Python_Homework5\\decoded_text.txt"    # восстановленный текст
print(read_data(input_text))  # исходный текст
print(encode_rle(read_data(input_text))) # сжатый текст
with open(str(tx), "w", encoding="UTF-8") as data:
    data.write(encode_rle(read_data(input_text)))
print(decode_rle(read_data(tx))) # восстановленный текст
with open(str(text1), "w", encoding="UTF-8") as data:
    data.write(decode_rle(read_data(tx)))
