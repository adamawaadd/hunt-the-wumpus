# 2D Hunt the Wumpus – Terminal Game

A **terminal-based 2D implementation of Hunt the Wumpus** in Python. Navigate a grid, avoid hazards, and hunt the Wumpus, all from your terminal. Created as a class assignment.

## Features
- **2D Grid Gameplay**: Explore a randomized cave with hidden hazards that can be played in regular or debug mode!
- **Hazards**: Avoid pits and bats. Bats can make you **confused**, inverting movement and arrow firing for 5 turns. Bottomless pits have a 50% chance of killing you.
- **Arrow Mechanics**: Strategically shoot arrows to try to slay the Wumpus or find the treasure and escape up the rope.
- **Replayable**: Each game randomizes the Wumpus and hazard placement.  
- **Terminal-Based UI**: Fully playable without any graphics.

## How to Play
1. Clone the repository.
2. Navigate to the project directory:
```
cd hunt-the-wumpus
```
3. Run the game:
```
python main.py
```
4. Move with W/A/S/D keys and shoot arrows using F, then W/A/S/D.
5. Survive hazards and hunt the Wumpus to win.
