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

