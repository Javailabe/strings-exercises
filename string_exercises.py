# # zad 1, first letter capital
# text = input('Podaj tekst: ')
# text = 'python'
# modified_text = text[0].upper() + text[1:]
# print(modified_text)
from operator import truediv

# # zad 2, count a
# count = 0
# # text = input('Podaj tekst: ')
# text = 'ananas'
# for char in text:
#     if char == 'a':
#         count += 1
# print('a wystepuje: ' + str(count))

# # zad 3, revert
# # text = input('Podaj tekst: ')
# text = 'kot'
# reversed_text = text[::-1]
# print(reversed_text)

# # zad 4, palidrome check
# # text = input('Podaj tekst: ')
# text = 'kajak'
# processed_text = text[::-1]
# print('is plaindrome: ' + str(text == processed_text))

# # zad 5, spaces to -
# # text = input('Podaj tekst: ')
# text = 'Ala ma kota'
# replaced_text = text.replace(' ', '-')
# print(replaced_text)

# # zad 6, sum for each char
# text = input('Podaj liczbe calkowita: ')
# sum = 0
# for char in text:
#     num = int(char)
#     sum += num
# print(f'suma liczb z ciągu {text} to ' + str(sum))

# # zad 7, czy parzysta
# text = input('Podaj liczbe calkowita: ')
# number = int(text)
# print(f'czy {number} jest parzyste? {number % 2 == 0}')

# # zad 8, silnia
# text = input('Podaj liczbe calkowita: ')
# number = int(text)
# if number < 0:
#     print('silni nie liczy sie dla liczb mniejszych niz 0')
# elif number == 0:
#     print(f'silnia {number} = ' + str(1))
# else:
#     value = 1
#     for i in range(1, number + 1):
#         value *= i
#     print(f'silnia {number} = ' + str(value))

# # zad 9, najwieksza z ciagu
# text = input('Podaj liczbe calkowita: ')
# numbers = list(text)
# maximum = max(numbers)
# print(maximum)

# # zad 10, liczba na binarne
# text = input('Podaj liczbe calkowita: ')
# number = int(text)
# binary_format = bin(number)[2:]
# print(binary_format)

# # zad 11, zlicz slowa
# # text = input('Napisz zdanie: ')
# test_string = 'To jest przykładowe zdanie'
# table_text = test_string.split(' ')
# print(f'ilosc slow w zdaniu {test_string} to {len(table_text)}')

# # zad 12, usun cyfry
# # text = input('Napisz cos: ')
# test_string = 'asdhj123ghk89kdjf34'
# non_int_string = ''
# for char in test_string:
#     if not char.isdigit():
#         non_int_string += char
# print(non_int_string)

# # zad 13, sprawdz czy tylko litery
# # # text = input('Napisz cos: ')
# # test_string = 'asdhj123ghk89kdjf34'
# test_string = 'ala ma kota'
# letters_only = True
# for char in test_string:
#     if not char.isdigit():
#         letters_only = True
#     else:
#         letters_only = False
#         break
# print(f'czy string "{test_string}" sklada sie tylko z liter? {letters_only}')