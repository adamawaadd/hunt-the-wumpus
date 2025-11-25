import random
from typing import Optional
from player import Player
from event import Event
from room import Room
from game import Game

def main() -> None:
    game = Game()
    debug_mode = game.get_debug_mode()

    events: list[Event] = []
    game.create_events(events)

    game_map: list[list[Room]] = []
    game.create_map(game_map)
    

    game.fill_events(events, game_map)
    game.fill_empty_rooms(game_map)

    while True: 
        game.player_round(game_map)
        if game.get_won():
            break
        elif game.get_lost():
            break

if __name__ == '__main__':
    main()