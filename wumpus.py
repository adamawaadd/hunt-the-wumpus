from typing_extensions import override
from event import Event
from player import Player

class Wumpus(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("A stench permeates the air.")

    @override
    def encounter(self, player: Player) -> None:
        print("You encountered the Wumpus and were eaten.")
        player.died()