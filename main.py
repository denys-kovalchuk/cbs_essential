from game import Game
import art
import time


if __name__ == '__main__':
    game = Game()
    art.tprint('Welcome to Blackjack')
    print('__________________________________________')
    time.sleep(1)
    game.deck.shuffle_deck()
    p = game.add_players()
    print('__________________________________________')
    time.sleep(1)
    while True:
        game.bank_validator()
        game.place_bet()
        print('__________________________________________')
        time.sleep(1)
        for _ in range(2):
            game.deal_cards()
        print('__________________________________________')
        time.sleep(1)
        game.see_player_hand()
        print('__________________________________________')
        time.sleep(1)
        game.deal_more()
        print('__________________________________________')
        time.sleep(1)
