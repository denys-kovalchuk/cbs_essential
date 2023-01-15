import random
from settings import NAMES


class Player:
    def __init__(self, name, bank):
        self.hand = []
        self.name = name
        self.bank = bank
        self.count = 0

    def place_bet(self):
        print(f'\nYou have {self.bank} dollars left. How much would you like to bet?')
        amount = input('Type a number of dollars to bet: ')
        if int(amount) > self.bank:
            print('You cannot bet more than you have, try again')
            self.place_bet()
        self.bank -= int(amount)
        return int(amount)

    def see_hand(self):
        for card in self.hand:
            print(f'You have {card}')


class Bot:
    def __init__(self):
        self.name = random.choice(NAMES)
        self.bank = random.randrange(50, 200, 10)
        self.hand = []
        self.count = 0

    def place_bet(self):
        if self.bank <= 20:
            amount = self.bank
            print(f'{self.name} places {amount} dollars. {self.bank - amount} dollars left')
            self.bank -= amount
            return amount
        else:
            amount = random.randrange(10, int(self.bank / 2), 10)
            print(f'{self.name} places {amount} dollars. {self.bank - amount} dollars left')
            self.bank -= amount
            return amount

    def see_hand(self):
        for card in self.hand:
            print(f'{self.name} has {card}')
