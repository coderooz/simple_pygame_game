
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

## Code Used: 

### settings.py

This file will contain configuration settings for the game.

```python
# settings.py

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player settings
PLAYER_SIZE = 50
PLAYER_SPEED = 10

# Enemy settings
ENEMY_SIZE = 50
ENEMY_SPEED = 10
```

### game.py

This file will contain the main game logic, including the game loop and class definitions for the player and enemies.

```python
# game.py

import pygame
import random
from settings import *

class Player:
    def __init__(self):
        self.size = PLAYER_SIZE
        self.color = RED
        self.pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * self.size]
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.pos[0] > 0:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT] and self.pos[0] < SCREEN_WIDTH - self.size:
            self.pos[0] += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

class Enemy:
    def __init__(self):
        self.size = ENEMY_SIZE
        self.color = WHITE
        self.pos = [random.randint(0, SCREEN_WIDTH - self.size), 0]
        self.speed = ENEMY_SPEED

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > SCREEN_HEIGHT:
            self.pos = [random.randint(0, SCREEN_WIDTH - self.size), 0]
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simple Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 72)
        self.reset_game()

    def reset_game(self):
        self.player = Player()
        self.enemy = Enemy()
        self.running = True
        self.score = 0
        self.game_over = False

    def run(self):
        while True:
            self.events()
            if self.running:
                self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                mouse_pos = event.pos
                if self.replay_button.collidepoint(mouse_pos):
                    self.reset_game()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        if self.enemy.move():
            self.score += 1
        self.check_collision()

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.draw_score()
        if self.game_over:
            self.draw_game_over()
        pygame.display.flip()

    def check_collision(self):
        if self.player.get_rect().colliderect(self.enemy.get_rect()):
            self.game_over = True
            self.running = False

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        game_over_text = self.big_font.render("Game Over", True, RED)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        
        replay_text = self.font.render("Replay", True, WHITE)
        self.replay_button = pygame.Rect(SCREEN_WIDTH // 2 - replay_text.get_width() // 2, SCREEN_HEIGHT // 2 + game_over_text.get_height(), replay_text.get_width(), replay_text.get_height())
        pygame.draw.rect(self.screen, BLACK, self.replay_button)
        self.screen.blit(replay_text, (self.replay_button.x, self.replay_button.y))

```

### main.py

This file will be the entry point to start the game.

```python
# main.py

from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
```

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
