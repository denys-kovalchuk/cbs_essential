from faker import Faker


SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
NAMES = [Faker().first_name() for _ in range(10)]
THRESHOLD = 17
