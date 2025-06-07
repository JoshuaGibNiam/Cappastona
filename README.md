# Project Cappastona

---

## Description & Overview
This is a capstone project for my python project, and (probably) is the biggest coding project
I've ever written. I started this in April (I don't know the exact date) and the project has 
accumulated to over 1,000 lines of code. This project mainly utilizes the *ttkbootstrap* and *pygame* module
to create a stealth action game.

---

## Tutorial
The objective of the game is to kill all the enemies and enter the portal after, while avoiding getting spotted. 
Your highscore will be higher if you finish within a shorter time.
1. Move your player across the 2D map by using WASD or the arrow keys. There are walls to block your path, and of
course world border constraints.
2. You will see enemies patrolling the map in set paths. Each enemy has an FOV (field of view) and you should avoid
having contact with these red triangle FOVs (If you do you die). Instead, you should sneak up on the enemy from behind
where it cannot see you to kill him.
3. After killing all the enemies, you need to walk to the portal to complete the level.

P.S. as of today there are only 5 levels, cuz creating a level consumes much time.

---

## Code
This program is made up of 17 files excluding this, as follows:
1. `main.py`: The only `.py` file that uses ttkbootstrap and tkinter. This file includes the title screen,
login screen and sign up screen. To start playing, you have to log into (or sign up) an account, then press the green
"launch cappastona" button.
2. `game.py`: Runs the game after pressing launch cappastona. This file has 4 functions:
    1. `run_game()`: handles fps, sprite updates and window bliting.
   2. `hard_quit()`: quits the game smoothly.
   3. `set_fps()`: a setter(?) method which controls the frame rate.  *
   4. `set_volume()`: a setter(?) method which controls the volume.   *
3. `player.py`: Sprite class: Handles the player sprite. This file is used in `game.py`.
4. `enemies.py`: Sprite class: Handles the enemy sprite, allowing it to turn and follow its path. Includes `enemy_1` class and
`enemy_1_fov` class, both of which are used in `game.py`.
5. `wall.py`: Sprite class: manages walls. Used in `game.py`.
6. `portal.py`: Sprite class: manages the portal. Used in `game.py` and `game_manager.py`.
7. `game_manager.py`: manages overall gameplay, including sound effects, win/lose detection, and highscore calculations. Used in `game.py`.
8. `constants.py`: a unique class which handles the CONSTANTS of the game, including FPS, WINDOW_HEIGHT and WINDOW_WIDTH. Also used to load level information, like
player spawn point and enemy paths. Used in `game.py`.
9. `testing_playground.py`: a place for debugging/testing. No code inside.
10. `accounts.json`: a json dict file, stores all the accounts' information. Used in `main.py`.
11. `levels.json`: a json file that stores all the level information. The format used is:
   - level number:
     - portal : spawn point
     - player:
       - spawn point : [x, y]
     - enemies:
       - enemy number: 
         - spawn point : [x, y]
         - path : [[(x, y), True], ...]  # True/False = move horizontally (True) or vertically (False)
         - starting angle: angle
     - walls:
       - wall number : "Wall(x, y, width, height)"
   This file is used in `constants.py`

Nos 12-17. is the remaining images and sound effects used.

---

## How to run
1. Clone this repository:
```
git clone https://github.com/JoshuaGibNiam/Cappastona
```
2. Run the game at:
`main.py`

---

## Future updates
1. Finish setting system.
2. Allow for skins
3. More types of enemies
4. Time limit
5. Power-ups

---

### Credits
Me myself, and ChatGpt

---

7/6/2025, 2:36 p.m.