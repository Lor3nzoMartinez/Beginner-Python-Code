def one_letter_per_line(word):
    for ndx in range (len(word)):
        print(word[ndx])

words = ['tiger','parrot','computer']
for word in words:
    one_letter_per_line(word)
    print()

def numeric_value_ofL(Letter):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    letter_value =  alpha.find(Letter.lower())
    return letter_value

alpha = 'abcdefghijklmnopqrstuvwxyz'
for Letter in alpha:
    print(Letter,numeric_value_ofL(Letter))


def numeric_value_ofW(Word):
    word_value = 0
    for Letter in Word:
        word_value += numeric_value_ofL(Letter)
    return word_value

print(numeric_value_ofW('cat'))
