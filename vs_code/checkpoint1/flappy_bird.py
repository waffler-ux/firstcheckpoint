import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 5
SPAWN_RATE = 90

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.width = 30
        self.height = 30
        self.velocity = 0
    
    def flap(self):
        self.velocity = FLAP_STRENGTH
    
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
    
    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, (self.x, self.y, self.width, self.height))
        # Draw eye
        pygame.draw.circle(surface, BLACK, (self.x + 20, self.y + 10), 3)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = PIPE_WIDTH
        gap_pos = random.randint(100, SCREEN_HEIGHT - 100 - PIPE_GAP)
        self.gap_top = gap_pos
        self.gap_bottom = gap_pos + PIPE_GAP
    
    def update(self):
        self.x -= PIPE_SPEED
    
    def draw(self, surface):
        # Top pipe
        pygame.draw.rect(surface, GREEN, (self.x, 0, self.width, self.gap_top))
        # Bottom pipe
        pygame.draw.rect(surface, GREEN, (self.x, self.gap_bottom, self.width, SCREEN_HEIGHT - self.gap_bottom))
    
    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.gap_top)
    
    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.gap_bottom, self.width, SCREEN_HEIGHT - self.gap_bottom)
    
    def is_offscreen(self):
        return self.x + self.width < 0

class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.spawn_counter = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.__init__()
                    else:
                        self.bird.flap()
        return True
    
    def update(self):
        if self.game_over:
            return
        
        self.bird.update()
        
        # Check boundaries
        if self.bird.y <= 0 or self.bird.y + self.bird.height >= SCREEN_HEIGHT:
            self.game_over = True
        
        # Spawn pipes
        self.spawn_counter += 1
        if self.spawn_counter >= SPAWN_RATE:
            self.pipes.append(Pipe(SCREEN_WIDTH))
            self.spawn_counter = 0
        
        # Update pipes
        for pipe in self.pipes:
            pipe.update()
        
        # Remove offscreen pipes
        for pipe in self.pipes[:]:
            if pipe.is_offscreen():
                self.pipes.remove(pipe)
                self.score += 1
        
        # Collision detection
        bird_rect = self.bird.get_rect()
        for pipe in self.pipes:
            if bird_rect.colliderect(pipe.get_top_rect()) or bird_rect.colliderect(pipe.get_bottom_rect()):
                self.game_over = True
    
    def draw(self):
        screen.fill((135, 206, 235))  # Sky blue background
        
        self.bird.draw(screen)
        for pipe in self.pipes:
            pipe.draw(screen)
        
        # Draw score
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Draw game over screen
        if self.game_over:
            game_over_text = font.render("GAME OVER!", True, RED)
            restart_text = font.render("Press SPACE to restart", True, BLACK)
            final_score_text = font.render(f"Final Score: {self.score}", True, BLACK)
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 60))
            screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 + 60))
        
        pygame.display.flip()

def main():
    game = Game()
    running = True
    
    while running:
        running = game.handle_events()
        game.update()
        game.draw()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
