from random import randint

print(randint(1,6))

'''
def roll_dice():
        return (randint(1,6))

for i in range(10):
    print(roll_dice(),end = ",")

def roll_Dice_pair():
    return(randint(1,6)+randint(1,6))


def playDice():
    result = roll_Dice_pair()
    n_rolls = 1

    while result != 2:
        result = roll_Dice_pair()
        n_rolls = n_rolls + 1

    return n_rolls, 100 - n_rolls - 1

for i in range (5):
    n_rolls, score = playDice()
    print(n_rolls,score)


def playDiceGame():
    rollDiceResult = roll_dice()
    sum_acum = 0
    n_rolls = 1
    avg = 0
    while rollDiceResult != 2:
        rollDiceResult = roll_dice()
        n_rolls = n_rolls + 1
        sum_acum = sum_acum + (100-(n_rolls - 1))
    avg = sum_acum / n_rolls
    return avg

for i in range (3):
    avg_score = playDiceGame()
    print('Avg score was ', avg_score)
'''
