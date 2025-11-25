import random
from typing_extensions import override
from event import Event
from player import Player

class BottomlessPit(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("You feel a breeze.")

    @override
    def encounter(self, player: Player) -> None:
        deadly = random.randint(0, 1)
        if deadly == 1:
            print("You avoided the bottomless pit and survived!")
        else:
            print("You fell into a bottomless pit and died.")
            player.died()