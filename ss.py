word = input('Введите слово')
probe = input()
new_word = word
while word:
    if word.count(word[0]) > 1:
        alfa = word[0]
        new_word = new_word.replace(alfa, '*')
    word = word.replace(word[0], '')

print(new_word)

a = len(probe)
print(a)
probe = probe.replace(probe[0], '')
b = len(probe)
print(b)
print(probe)
