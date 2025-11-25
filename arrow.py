from typing_extensions import override
from event import Event
from player import Player

class Arrow(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("You step on something sharp. Ouch!")

    @override
    def encounter(self, player: Player) -> None:
        if super().get_active():
            player.add_arrow()
            print(f"You picked up 1 arrow! Current Arrows: {player.get_arrow()}")
            super().set_inactive()
        else:
            pass
        