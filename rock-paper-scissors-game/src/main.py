import pygame
import sys
from game.logic import determine_winner, get_computer_choice
from game.ui import draw_game, show_result

def get_user_choice_gui(screen):
    font = pygame.font.Font(None, 36)
    choices = ["Rock", "Paper", "Scissors"]
    buttons = []

    # Create buttons for each choice
    for i, choice in enumerate(choices):
        button_rect = pygame.Rect(100 + i * 200, 400, 150, 50)
        buttons.append((button_rect, choice))

    while True:
        screen.fill((0, 0, 0))  # Clear the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
                print(f"Mouse clicked at: {mouse_pos}")  # Debugging output
                for button_rect, choice in buttons:
                    if button_rect.collidepoint(mouse_pos):  # Check if the mouse click is inside a button
                        print(f"Button clicked: {choice}")  # Debugging output
                        return choice

        # Draw buttons
        for button_rect, choice in buttons:
            pygame.draw.rect(screen, (0, 128, 255), button_rect)  # Draw button rectangle
            pygame.draw.rect(screen, (255, 255, 255), button_rect, 2)  # Add a border to the button
            text = font.render(choice, True, (255, 255, 255))  # Render button text
            text_rect = text.get_rect(center=button_rect.center)  # Center the text in the button
            screen.blit(text, text_rect)  # Draw the text on the screen

        pygame.display.flip()  # Update the display

def main():
    try:
        pygame.init()
    except pygame.error as e:
        print(f"Failed to initialize pygame: {e}")
        sys.exit(1)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rock-Paper-Scissors Game")

    clock = pygame.time.Clock()
    running = True
    user_choice = None
    computer_choice = None
    result = None

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Get user choice via GUI
            if user_choice is None:
                user_choice = get_user_choice_gui(screen)
                computer_choice = get_computer_choice()
                result = determine_winner(user_choice, computer_choice)

            # Draw the game state and result
            draw_game(screen, user_choice, computer_choice)
            show_result(screen, result)

            pygame.display.flip()
            clock.tick(60)

            # Reset choices after showing the result for a while
            pygame.time.wait(2000)  # Wait for 2 seconds
            user_choice = None
            computer_choice = None
            result = None

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()