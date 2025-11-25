from abc import ABC, abstractmethod
from player import Player

class Event(ABC):
    _character: str
    _active: bool
    _debug: bool
    _row: int
    _column: int

    def __init__(self, character: str, debug_mode: bool) -> None:
        self._character = character
        self._active = True
        self._debug = debug_mode
        self._arrow_count = 0

    def get_character(self) -> str:
        return self._character

    def get_active(self) -> bool:
        return self._active

    def set_inactive(self) -> None:
        self._active = False
        self._character = " "

    def set_position(self, row: int, column: int) -> None:
        self._row = row
        self._column = column

    @abstractmethod
    def get_percept(self) -> None:
        pass
    
    @abstractmethod
    def encounter(self, player: Player) -> None:
        pass
