
## Simple Pygame Project

This is a simple game developed using Python and Pygame. In this game, the player controls a red block that can move left and right to avoid collision with the falling white blocks. The game continues until the player collides with a white block, at which point the game ends and the player can choose to replay. The player earns points for every white block that passes without colliding.

### Features
- **Player Movement**: Use the left and right arrow keys to move the red block.
- **Enemies**: White blocks fall from the top of the screen at a constant speed.
- **Score System**: Earn points for every enemy that moves past the player without collision.
- **Game Over Screen**: Displays "Game Over" and shows a replay button to restart the game.
- **Replay Functionality**: Allows the player to start a new game without restarting the program.

### How to Run
1. Ensure you have Python and Pygame installed. You can install Pygame using the following command:
   ```sh
   pip install pygame
   ```
2. Clone the repository:
   ```sh
   git clone https://github.com/coderooz/simple_pygame_game.git
   ```
3. Navigate to the project directory:
   ```sh
   cd simple-pygame-game
   ```
4. Run the game:
   ```sh
   python main.py
   ```

### File Structure
```
simple_pygame_game/
├── main.py
├── game.py
└── settings.py
```


### Explanation

1. **settings.py**: Contains all the configuration settings for easy adjustments.
2. **game.py**: 
   - `Player` and `Enemy` classes encapsulate the behavior and properties of the game objects.
   - `Game` class manages the game loop, event handling, updates, and drawing.
3. **main.py**: Starts the game by creating an instance of `Game` and calling its `run` method.

### Running the Game

To run the game, execute the `main.py` file:

```sh
python main.py
```

- **main.py**: The entry point of the game. Initializes and starts the game.
- **game.py**: Contains the main game logic, including the game loop, player and enemy classes, and collision detection.
- **settings.py**: Configuration file for game settings like screen dimensions, colors, and speeds.

### Future Improvements
- Add multiple enemies.
- Increase the difficulty over time by increasing enemy speed.
- Add sound effects and background music.
- Implement a high score system.

### Contributing
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
