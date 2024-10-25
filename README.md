# Pong-game 🏓

This project is a Python implementation of the classic Pong game using the Turtle graphics library. Two players control paddles to keep the ball in play. The game tracks the score, updates the speed of the ball, and includes collision detection with the paddles and walls.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

## Features

- **Two-Player Mode**: Controls for both players to move paddles up and down.
- **Dynamic Ball Movement**: The ball bounces off walls and paddles and increases speed with each paddle hit.
- **Score Tracking**: A scoreboard displays the score for each player.
- **Game Over Detection**: The ball resets when missed by a paddle, and the score updates accordingly.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/pong_game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd pong_game
    ```

3. Ensure Python 3.x is installed and has Turtle graphics support.

## Usage

1. Run the `main.py` script:
    ```bash
    python main.py
    ```

2. Use the following controls for paddle movement:
   - **Right Paddle**: Press the `Up` arrow to move up, `Down` arrow to move down.
   - **Left Paddle**: Press `W` to move up and `S` to move down.

## Modules

### `ball.py`
Defines the `Ball` class, which handles ball movement, speed adjustment, and collision detection with the paddles and walls.

### `main.py`
The main game loop, creating the screen, initializing the game objects, and handling user input and gameplay.

### `paddle.py`
Defines the `Paddle` class, which manages paddle movement and initialization.

### `scoreboard.py`
Defines the `Scoreboard` class to track and display the scores for each player.
