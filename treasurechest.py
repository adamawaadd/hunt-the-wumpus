from typing_extensions import override
from event import Event
from room import Room
from player import Player

class TreasureChest(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("You see something shimmer in the distance.")

    def get_character(self) -> str:
        return super().get_character()

    @override
    def encounter(self, player: Player) -> None:
        if super().get_active():
            print("You picked up a treasure chest!")
            player.holding_treasure()
            super().set_inactive()
        else:
            pass