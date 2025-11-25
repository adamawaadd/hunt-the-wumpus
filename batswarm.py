from typing_extensions import override
from event import Event
from player import Player

class BatSwarm(Event):

    def __init__(self, character: str, debug_mode: bool) -> None:
        super().__init__(character, debug_mode)

    @override
    def get_percept(self) -> None:
        print("You hear wings flapping.")

    @override
    def encounter(self, player: Player) -> None:
        print("You found a bat swarm and you're disoriented!")
        player.set_lost()
