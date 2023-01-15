import art
from cards import Deck
from players import Player, Bot
from settings import THRESHOLD


class Counter(Deck):
    def __init__(self, hand):
        super().__init__()
        self.hand = hand
        self.total = 0

    def count(self):
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                self.total += 10
            if card.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                self.total += int(card.rank)
            if card.rank == 'A':
                if self.total <= 11:
                    self.total += 11
                else:
                    self.total += 1
        return self.total


class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.total_bank = 0
        self.lost = []

    def add_players(self):
        name = input('Enter your name: ').capitalize()
        bank = input('Enter your bank amount: ')
        human = Player(name, int(bank))
        print('How many players do you want to add?')
        bots_count = input('Type a number of players to add: ')
        for _ in range(int(bots_count)):
            bot = Bot()
            self.players.append(bot)
        self.players.append(human)
        for player in self.players:
            print(f'Player {player.name}, money {player.bank} joined the game')
        return self.players

    def deal_cards(self):
        for player in self.players:
            deal = self.deck.deal_cards()
            player.hand.append(deal)
        return self.deck

    def see_player_hand(self):
        for player in self.players:
            player.see_hand()

    def place_bet(self):
        self.total_bank = 0
        for player in self.players:
            self.total_bank += player.place_bet()

    def count(self):
        for player in self.players:
            res = Counter(player.hand)
            res.count()
            print(f'{player.name} has {res.total}')
            player.count = res.total
            if player.count > 21:
                print(f'Player {player.name} lost, they have {player.count}')

    def deal_more(self):
        self.count()
        for player in self.players:
            if isinstance(player, Bot):
                if player.count < THRESHOLD:
                    deal = self.deck.deal_cards()
                    player.hand.append(deal)

            if isinstance(player, Player):
                if player.count > 21:
                    return self.winner()
                print('Would you like to have more cards?')
                more = input('Type [y/n]: ')
                if more == 'y':
                    deal = self.deck.deal_cards()
                    player.hand.append(deal)
                    self.see_player_hand()
                    self.deal_more()
                else:
                    return self.winner()

    def winner(self):
        totals = [player.count for player in self.players if player.count <= 21]
        if not totals:
            self.total_bank = 0
            self.hand_reset()
        else:
            winners = [player for player in self.players if player.count == max(totals)]
            art.tprint('Winner-winner chicken dinner')
            for player in winners:
                print(f'Winner-winner chicken dinner, player {player.name} won')
                print(f'Total win is {self.total_bank} dollars. Winner gets {self.total_bank / len(winners)} dollars')
                player.bank += self.total_bank / len(winners)
            self.total_bank = 0
            self.hand_reset()

    def hand_reset(self):
        self.deck = Deck()
        for player in self.players:
            player.hand = []

    def bank_validator(self):
        for player in self.players:
            if player.bank <= 0:
                print(f'{player.name} has lost and left the game')
                self.players.remove(player)
