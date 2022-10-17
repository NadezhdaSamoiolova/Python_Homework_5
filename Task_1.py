# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# input_str = input()
# text1 = 'абв'
# input_list = input_str.split()
# result_list = []
# for word in input_list:
#     if text1 not in word:
#         result_list.append(word)
# print(' '.join(result_list))


#### С помощью функции
def word_remove(my_str, symbols):
    return(' '.join([word for word in my_str.split() if symbols not in word]))

my_str = input('Input your text: ')
symbols = 'абв'
print(word_remove(my_str, symbols))

