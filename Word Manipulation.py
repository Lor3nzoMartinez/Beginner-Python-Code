
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

print(numeric_value_ofW('Bob'))

def up(Word):
    Ln = len(word)
    for ndx in range (1,Ln):
        print(Word[:ndx])

def down(Word):
    Ln = len(Word)
    for ndx in range (Ln-1,0,-1):
        print(Word[:ndx])

def updown(Word):
    up(Word)
    print(Word)
    down(Word)

def up(Word):
    x = 0
    while x < len(Word):
        x += 1
        print(Word[:x])
              
def down(Word):
    x = len(Word) 
    while x > 0:
        x -= 1
        print(Word[:x])

def updown(Word):
    up(Word)
    down(Word)

updown('encyclopedia')

