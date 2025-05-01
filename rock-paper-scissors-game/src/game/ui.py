import pygame
import sys

def draw_game(screen, user_choice, computer_choice):
    font = pygame.font.Font(None, 48)
    screen.fill((0, 0, 0))  # Clear the screen

    user_text = font.render(f"User: {user_choice}", True, (255, 255, 255))
    computer_text = font.render(f"Computer: {computer_choice}", True, (255, 255, 255))

    screen.blit(user_text, (50, 200))
    screen.blit(computer_text, (50, 300))

def show_result(screen, result):
    font = pygame.font.Font(None, 72)
    result_text = font.render(result, True, (255, 255, 0))
    screen.blit(result_text, (50, 400))

class GameUI:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Rock-Paper-Scissors Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.running = True

    def display_message(self, message):
        self.screen.fill((255, 255, 255))
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()