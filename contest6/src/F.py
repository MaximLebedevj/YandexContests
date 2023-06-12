from itertools import product

c = ['пик', 'треф', 'бубен', 'червей']
cin = input()
c = [x for x in c if x != cin]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама',
         'король', 'туз']
for i in product(cards, c):
    print(f'{i[0]} {i[1]}')

