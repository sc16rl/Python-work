import random

card_type = ('heart','spades','club','diamond')

card_num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def produce():
    Pairs = []
    for type in card_type:
        for num in card_num:
            Pairs.append((type, num))

    Pairs.append(('joker', 'big'))
    Pairs.append(('joker', 'small'))

    random.shuffle(Pairs)
    A = Pairs[0:17]
    B = Pairs[17:34]
    C = Pairs[34:51]
    remain = Pairs[51:54]

    print("Player A:        ", A)
    print("Player B:        ", B)
    print("Player C:        ", C)
    print("Remaining cards: ", remain)
    return

while True:
    user_operation = input("Shuffle cards?\n yes or no")
    if user_operation == 'yes':
        produce()
    elif user_operation == 'no':
        break
    else:
        continue