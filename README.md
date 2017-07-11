# Py-Climber
**_Py-Climber_** is a simple game written as a learning project for Python using the pygame module.  It is **_vaguely_** inspired by the game Ice-Climber for the NES.  I am not new to programming, but I am a neophyte when it comes to python.  This means while I've tried to embrace the python way of doing things, I probably regressed in places due to old habits in other languages.

**Objective:** Reach the top level by breaking blocks from beneath, then jumping on top.  Avoid the green blob enemies which will send you back to the bottom.

*Demo*

![](http://i.imgur.com/ucUYc06.gif)

## Running the Game
You will need the pygame and python3 files installed, as well as the images from my repository (e.g. .\\images\\*) wherever you copy the scripts.  Cloning the repository is the easiest method, or download the whole thing.  I don't have a lot of "extra" stuff in the repo

```
python pyclimber.py
```

## File Descriptions
Each file contains only one class, or a collection of related functions.  The brief overview of each is listed below.

### pyclimber.py
This is the main entry point for the game.  It creates the top level objects and contains the main game loop.  Start here if you want to trace through execution via code inspection or the debugger.

### game_functions.py
Inspired by a project in the *Python Crash Course* book, this module holds common game functions you're likely find in the main loop, such as updating all objects, drawing all objects, handling input, etc.

### settings.py
Likewise inspired - this caches common settings for the game, such as the dimensions of a tile, the player sprite attributes, etc

### image_resources.py
Loads images from disk and caches them for later use.  Also has a helper to split images into a list of frames for animated sprites.

### tilemap.py
This is a traditional 2D tilemap.  It takes a list of tiles (loaded via image_resources) and a list of integers representing a layout.  The tilemap also owns the block objects the player will break and/or stand on.

### block.py
The simplest of sprites: it has only 1 image and once placed never moves.  It can only be removed, or used as a platform.

### animation.py
Tracks animation sequences for sprites with multiple sets of frames (walking left vs right vs jumping, etc).  This really boils down to managing a list of integers.  Not exciting, but needed.

### animated_sprite.py
This is a base-class shared by the 2 classic sprites in the game (the player and the enemies).  Common physics code (simple gravity) and bounds/collision checking is done here.  There are hooks to allow the derived classes to behave differently on updates or collisions.

### blob_enemy.py
The simplest of animated sprites, it only has 3 modes: walking left, walking right, and falling.  It shares common collision detection for the map boundary and the blocks, but it alone can fall through the lower grate.

### player.py
A more complex animated sprite.  The player has more animations, reacts to input from the user, and must interact with the block objects to both destroy (from the bottom) or stand on (from the top).





