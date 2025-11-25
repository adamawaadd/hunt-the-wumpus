class Player:
    _icon: str
    _player_row: int
    _player_column: int
    _is_alive: bool
    _is_lost: bool
    _turns_lost: int
    _holding_treasure: bool
    _arrow_count: int
    _win: bool
    _lose: bool
    _has_moved: bool

    def __init__(self) -> None:
        self._icon = "*"
        self._is_alive = True
        self._is_lost = False
        self._holding_treasure = False
        self._player_row = 0
        self._player_column = 0
        self._win = False
        self._lose = False
        self._arrow_count = 0
        self._has_moved = False

    def set_position(self, row: int, column: int) -> None:
        self._player_row = row
        self._player_column = column

    def get_row(self) -> int:
        return self._player_row

    def get_column(self) -> int:
        return self._player_column

    def get_player(self) -> str:
        return self._icon

    def died(self) -> None:
        self._is_alive = False
        self._lose = True

    def lost(self) -> bool:
        return self._lose

    def win(self) -> None:
        self._win = True

    def won(self) -> bool:
        return self._win

    def add_arrow(self) -> None:
        self._arrow_count += 1

    def subtract_arrow(self) -> None:
        self._arrow_count -= 1

    def get_arrow(self) -> int:
        return self._arrow_count

    def use_arrow(self) -> None:
        self._arrow_count -= 1

    def set_lost(self) -> None:
        self._is_lost = True
        self._turns_lost = 0

    def get_lost(self) -> bool:
        if self._is_lost:
            return True
        else: 
            return False

    def get_lost_num(self) -> int:
        return self._turns_lost

    def add_lost_turn(self) -> None:
        self._turns_lost += 1

    def reset_lost(self) -> None:
        self._is_lost = False
        self._turns_lost = 0

    def holding_treasure(self) -> None:
        self._holding_treasure = True

    def get_treasure_status(self) -> bool:
        return self._holding_treasure

    def check_rows(self) -> int:
        rows = 0
        valid_input = False
        while not valid_input:
            print("\nWelcome to Hunt the Wumpus!")
            try:
                rows = int(input("How many rows should the cave have?: "))
                if rows >= 4 and rows <= 20:
                    valid_input = True
                else:
                    raise TypeError("Please have between 4-20 rows!")
            except ValueError as e:
                print("Please enter a number!")
            except TypeError as e:
                print(e)
        return rows
    
    def check_columns(self) -> int:
        columns = 0
        valid_input = False
        while not valid_input:
            try:
                columns = int(input("How many columns should the cave have?: "))
                if columns >= 4 and columns <= 20:
                    valid_input = True
                else:
                    raise TypeError("Please have between 4-20 columns!")
            except ValueError as e:
                print("Please enter a number!")
            except TypeError as e:
                print(e)
        return columns

    def check_debug(self) -> bool:
        is_debug = False
        val = 99
        valid_input = False
        while not valid_input:
            try:
                val = int(input("Enter 1 for debug mode, 0 for normal mode: "))
                if val == 1 or val == 0:
                    valid_input = True
                else:
                    print("Please enter 1 or 0!")
            except ValueError as e:
                print("Please enter a number!")
        if val == 1:
            return True
        return False

    def has_moved(self) -> bool:
        return self._has_moved

    def reset_moved(self) -> None:
        self._has_moved = False

    def move(self, action: str) -> None:
        if action == "W":
            self._player_row -= 1
        elif action == "S":
            self._player_row += 1
        elif action == "A":
            self._player_column -= 1
        else:
            self._player_column += 1
        self._has_moved = True