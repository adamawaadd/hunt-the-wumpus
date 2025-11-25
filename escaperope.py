from typing_extensions import override
from event import Event
from player import Player

class EscapeRope(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("This place looks familiar...")

    @override
    def encounter(self, player: Player) -> None:
        treasure_status = player.get_treasure_status()
        if treasure_status == 1:
            print("You escaped! Congrats on surviving!")
            player.win()
        else:
            pass