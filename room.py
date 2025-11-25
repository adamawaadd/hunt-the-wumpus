from typing import Optional
from event import Event
from player import Player

class Room:
    _room: Optional[Event]
    _is_event: bool
    _row: int
    _column: int
    _total_rows: int
    _total_columns: int
    _is_debug: bool

    def __init__(self) -> None:
        self._room = None
        self._is_event = False
        self._row = -1
        self._column = -1
        self._is_debug = False
        self._total_rows = 0
        self._total_columns = 0

    def set_room(self, event: Event, row: int, column: int, debug: bool) -> None:
        self._room = event
        self._is_event = True
        self._row = row
        self._column = column
        self._is_debug = debug

    def set_empty_room(self, row: int, column: int, debug: bool) -> None:
        self._room = None
        self._is_event = False
        self._row = row
        self._column = column
        self._is_debug = debug
    
    def is_event(self) -> bool:
        if self._is_event == None:
            return False
        return self._is_event

    def is_percept(self) -> bool:
        if self._room is not None:
            if self._room.get_active():
                return True
            else:
                return False
        else:
            return False

    def get_event_type(self) -> str:
        if self._room == None:
            return " "
        return self._room.get_character()

    def get_char(self) -> str:
        if self._room == None:
            return " "
        elif self._is_debug and self._is_event:
            return self._room.get_character()
        return " "
    
    # Access the max row and max column size so printing to terminal is easier
    def map_size(self, row: int, col: int) -> None:
        self._total_rows = row
        self._total_columns = col

    def middle_cell(self, player_r: int, player_c: int) -> str:
        if self._row == player_r and self._column == player_c:
            player_char = "*"
        else:
            player_char = " "
        if self._room == None:
            room_char = " "
        elif self._is_debug:
            room_char = self._room.get_character()
        else:
            room_char = " "
        return f"{player_char}{room_char}|"

    def get_percept(self) -> None:
        if self._room is not None:
            self._room.get_percept()
        else:
            pass

    def enact_encounter(self, player: Player) -> None:
        if self._room is not None:
            self._room.encounter(player)
        else:
            pass

    def get_is_wumpus(self) -> bool:
        if self._room is not None:
            if self._room.get_character() == "W":
                return True
            else:
                return False
        else:
            return False