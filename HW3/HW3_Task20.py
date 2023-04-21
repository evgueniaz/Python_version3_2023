# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

d = dict.fromkeys(['a', 'b'], 100)
letter_values = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 
                               'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
letter_values.update(dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2))
letter_values.update(dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3))
letter_values.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 4))
letter_values.update(dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 5))
letter_values.update(dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8))
letter_values.update(dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10))

word = input("Enter a word to calculate its value >> ")
word = word.upper()
word_value = 0
for el in word: 
    word_value += letter_values.get(el) # type: ignore
print(f'The value of this word is {word_value}')

