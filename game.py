import random
from player import Player
from room import Room
from event import Event
from wumpus import Wumpus
from batswarm import BatSwarm
from bottomlesspit import BottomlessPit
from escaperope import EscapeRope
from treasurechest import TreasureChest
from arrow import Arrow

class Game(Player):
    _rows: int
    _columns: int
    _is_debug: bool
    _player: Player
    _game: bool

    def __init__(self) -> None:
        super().__init__()
        self._rows = super().check_rows()
        self._columns = super().check_columns()
        self._is_debug = super().check_debug()
        self._player = Player()
        print("\n")

    def get_rows(self) -> int:
        return self._rows

    def get_columns(self) -> int:
        return self._columns

    def get_debug_mode(self) -> bool:
        return self._is_debug
    
    def create_map(self, game_map: list[list[Room]]) -> None:
        for r in range(self._rows):
            row_list = []
            for c in range(self._columns):
                row_list.append(Room())
            game_map.append(row_list)
        
    def create_events(self, events: list[Event]) -> None:
        debug_mode = self.get_debug_mode()
        for _ in range(3):
            events.append(Arrow("A", debug_mode))
        for _ in range(2):
            events.append(BottomlessPit("P", debug_mode))
            events.append(BatSwarm("B", debug_mode))
        events.append(Wumpus("W", debug_mode))
        events.append(TreasureChest("T", debug_mode))
        events.append(EscapeRope("R", debug_mode))
    
    def fill_events(
                self, 
                events: list[Event], 
                game_map: list[list[Room]]) -> None:
        debug = self.get_debug_mode()
        for event in events:
            placed = False
            while placed == False:
                r = random.randint(0, self._rows - 1)
                c = random.randint(0, self._columns - 1)
                if not game_map[r][c].is_event():
                    game_map[r][c].set_room(event, r, c, debug)
                    game_map[r][c].map_size(self._rows, self._columns)
                    if event.get_character() == "R":
                        self._player.set_position(r, c)
                    placed = True


    def fill_empty_rooms(self, game_map: list[list[Room]]) -> None:
        debug = self.get_debug_mode()
        for r in range(self._rows):
            for c in range(self._columns):
                if not game_map[r][c].is_event():
                    game_map[r][c].set_empty_room(r, c, debug)
                    game_map[r][c].map_size(self._rows, self._columns)

    
    def print_all_rooms(self, game_map: list[list[Room]]) -> None:
        cols = self._columns
        player_r = self._player.get_row()
        player_c = self._player.get_column()
        for r in range(self._rows):
            print("----" + "---" * (cols - 1))
            print("|", end="")
            for c in range(cols):
                if c < cols - 1:
                    print(game_map[r][c].middle_cell(player_r, player_c), end="")
                else:
                    print(game_map[r][c].middle_cell(player_r, player_c))
        print("----" + "---" * (cols - 1))

    def player_round(self, game_map: list[list[Room]]) -> None:
        player_r = self._player.get_row()
        player_c = self._player.get_column()
        self.print_all_rooms(game_map)
        print("\n")
        self.check_percepts(game_map)
        if game_map[player_r][player_c].is_event():
            game_map[player_r][player_c].enact_encounter(self._player)
        if self._player.won() or self._player.lost():
            return
        self.movement(game_map)
        print("\n")


    def check_percepts(self, game_map: list[list[Room]]) -> None:
        player_row = self._player.get_row()
        player_col = self._player.get_column()
        if player_row < self._rows - 1:
            if game_map[player_row + 1][player_col].is_percept():
                game_map[player_row + 1][player_col].get_percept()
        if player_row > 0:
            if game_map[player_row - 1][player_col].is_percept():
                game_map[player_row - 1][player_col].get_percept()
        if player_col < self._columns - 1:
            if game_map[player_row][player_col + 1].is_percept():
                game_map[player_row][player_col + 1].get_percept()
        if player_col > 0:
            if game_map[player_row][player_col - 1].is_percept():
                game_map[player_row][player_col - 1].get_percept()

    def movement(self, game_map: list[list[Room]]) -> None:
        valid_action = False
        while valid_action == False:
            action = self.user_turn_input()
            if action == "F":
                arrow_action = self.user_arrow_input()
                if self._player.get_lost() and self._player.get_lost_num() <= 4:
                    valid_action = self.lost_arrow_action(arrow_action, game_map)
                else:
                    valid_action = self.reg_arrow_action(arrow_action, game_map)
            else:
                if self._player.get_lost() and self._player.get_lost_num() <= 5:
                    valid_action = self.lost_action(action, game_map)
                else:
                    valid_action = self.reg_action(action, game_map)

    def user_turn_input(self) -> str:
        while True:
            user_input = input("What would you like to do? (W/A/S/D to move, "
                                "F to fire an arrow): ")
            if user_input == "f" or user_input == "F":
                return "F"
            elif user_input == "w" or user_input == "W":
                return "W"
            elif user_input == "a" or user_input == "A":
                return "A"
            elif user_input == "s" or user_input == "S":
                return "S"
            elif user_input == "d" or user_input == "D":
                return "D"
            else:
                print("Invalid action.")

    def user_arrow_input(self) -> str:
        while True:
            user_input = input("What direction would you like to fire in? "
                                "(W/A/S/D): ")
            if user_input == "w" or user_input == "W":
                return "W"
            elif user_input == "a" or user_input == "A":
                return "A"
            elif user_input == "s" or user_input == "S":
                return "S"
            elif user_input == "d" or user_input == "D":
                return "D"
            else:
                print("Invalid action.")

    def can_complete_action(self, action: str) -> bool:
        while True:
            player_row = self._player.get_row()
            player_column = self._player.get_column()
            if action == "W" and player_row >= 1:
                return True
            elif action == "S" and player_row <= self._rows - 2:
                return True
            elif action == "A" and player_column >= 1:
                return True
            elif action == "D" and player_column <= self._columns - 2:
                return True
            else:
                print("Invalid direction.")
                return False

    def reverse_direction(self, action: str) -> str:
        if action == "W": return "S"
        if action == "A": return "D"
        if action == "S": return "W"
        if action == "D": return "A"
        else: return "F"

    def lost_arrow_action(self, arrow_action: str, game_map: list[list[Room]]) -> bool:
        if self._player.get_arrow() > 0:
            arrow_action = self.reverse_direction(arrow_action)
            self.fire_arrow(arrow_action, game_map)
            self._player.add_lost_turn()
            return True
        else:
            print("Out of arrows.")
            return False
    
    def lost_action(self, action: str, game_map: list[list[Room]]) -> bool:
            action = self.reverse_direction(action)
            return self.lost_direction(action)

    def lost_direction(self, action: str) -> bool:
        if self.can_complete_action(action):
            self._player.move(action)
            self._player.add_lost_turn()
            return True
        else: 
            return False

    def reg_arrow_action(self, arrow_action: str, 
                            game_map: list[list[Room]]) -> bool:
        if self._player.get_arrow() > 0:
            self.fire_arrow(arrow_action, game_map)
            return True
        else:
            print("Out of arrows.")
            return False


    def reg_action(self, action: str, game_map: list[list[Room]]) -> bool:
        return self.reg_direction(action)

    def reg_direction(self, action: str) -> bool:
        if self.can_complete_action(action):
            self._player.move(action)
            return True
        else:
            return False

    def fire_arrow(self, arrow_action: str, game_map: list[list[Room]]) -> None:
        self._player.reset_moved()
        if arrow_action == "W":
            self.fire_arrow_up(game_map)
        elif arrow_action == "S":
            self.fire_arrow_down(game_map)
        elif arrow_action == "A":
            self.fire_arrow_left(game_map)
        else:
            self.fire_arrow_right(game_map)


    def fire_arrow_up(self, game_map: list[list[Room]]) -> None:
        player_row = self._player.get_row()
        player_column = self._player.get_column()
        for i in range(3):
            if player_row - (i + 1) >= 0:
                if game_map[player_row - (i + 1)][player_column].get_is_wumpus():
                    print("The wumpus is defeated")
                    self._player.win()
                    return
            else:
                pass
        self._player.subtract_arrow()
        print(f"\nYou missed! You now have {self._player.get_arrow()} arrows.")

    def fire_arrow_down(self, game_map: list[list[Room]]) -> None:
        player_row = self._player.get_row()
        player_column = self._player.get_column()
        for i in range(3):
            if player_row + (i + 1) < self._rows:
                if game_map[player_row + (i + 1)][player_column].get_is_wumpus():
                    self._player.win()
                    print("The wumpus is defeated")
                    self._player.win()
                    return
            else:
                pass
        self._player.subtract_arrow()
        print(f"\nYou missed! You now have {self._player.get_arrow()} arrows.")

    def fire_arrow_left(self, game_map: list[list[Room]]) -> None:
        player_row = self._player.get_row()
        player_column = self._player.get_column()
        for i in range(3):
            if player_column - (i + 1) >= 0:
                if game_map[player_row][player_column - (i + 1)].get_is_wumpus():
                    self._player.win()
                    print("The wumpus is defeated")
                    self._player.win()
                    return
            else:
                pass
        self._player.subtract_arrow()
        print(f"\nYou missed! You now have {self._player.get_arrow()} arrows.")

    def fire_arrow_right(self, game_map: list[list[Room]]) -> None:
        player_row = self._player.get_row()
        player_column = self._player.get_column()
        for i in range(3):
            if player_column + (i + 1) < self._columns:
                if game_map[player_row][player_column + (i + 1)].get_is_wumpus():
                    self._player.win()
                    print("The wumpus is defeated")
                    self._player.win()
                    return
            else:
                pass
        self._player.subtract_arrow()
        print(f"\nYou missed! You now have {self._player.get_arrow()} arrows.")

    def get_won(self) -> bool:
        return self._player.won()

    def get_lost(self) -> bool:
        return self._player.lost()