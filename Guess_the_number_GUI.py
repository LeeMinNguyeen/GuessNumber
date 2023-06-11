import pygame
import random
import streamlit

# Initialize pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Heist")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font_title = pygame.font.SysFont("comicsans", 50)
font_guess = pygame.font.SysFont("comicsans", 30)

# Game variables
max_tries = 4
current_floor = random.randint(0, 9)
print(current_floor) ###
guesses_left = max_tries
game_over = False

# Main game loop
def game_loop():
    global guesses_left, game_over
    
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                check_guess(event.key)
        
        # Update display
        win.fill(WHITE)
        display_title()
        display_guesses()
        pygame.display.update()
    

def display_title():
    title_text = font_title.render("Diamond Heist", True, BLACK)
    win.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 50))

def display_guesses():
    global guesses_left, game_over
    
    guess_text = font_guess.render(f"Guesses left: {guesses_left}", True, BLACK)
    win.blit(guess_text, (WIDTH/2 - guess_text.get_width()/2, 200))
    
    if guesses_left == 0:
        result_text = font_guess.render(f"Game Over! The diamond was on floor {current_floor}.", True, RED)
        win.blit(result_text, (WIDTH/2 - result_text.get_width()/2, 300))
        pygame.display.update()
        pygame.time.wait(3000)
        game_over = True
    elif guesses_left == max_tries:
        introduction_text1 = font_guess.render("you are a theft trying to steal a diamond", True, BLACK)
        introduction_text2 = font_guess.render("in the museum that is 10 storey high but", True, BLACK)
        introduction_text3 = font_guess.render("you doesn't know which floor the diamond", True, BLACK)
        introduction_text4 = font_guess.render("is in. Try to guess the floor in 4 tries", True, BLACK)
        introduction_text5 = font_guess.render("Enter a floor number (0-9)", True, BLACK)                     
        win.blit(introduction_text1, (WIDTH/2 - introduction_text1.get_width()/2, 300))
        win.blit(introduction_text2, (WIDTH/2 - introduction_text2.get_width()/2, 330))
        win.blit(introduction_text3, (WIDTH/2 - introduction_text3.get_width()/2, 360))
        win.blit(introduction_text4, (WIDTH/2 - introduction_text4.get_width()/2, 390))
        win.blit(introduction_text5, (WIDTH/2 - introduction_text5.get_width()/2, 450))        
    else:
        guess_prompt_text2 = font_guess.render("Wrong floor", True, RED)        
        guess_prompt_text = font_guess.render("Try again. Enter your guess (0-9).", True, BLACK)
        win.blit(guess_prompt_text2, (WIDTH/2 - guess_prompt_text2.get_width()/2, 250))        
        win.blit(guess_prompt_text, (WIDTH/2 - guess_prompt_text.get_width()/2, 300))

def check_guess(key):
    global guesses_left
    
    try:
        guess=int(chr(key))
    except ValueError:
        pass
    else:
        if 0 <= guess <= 9:
            guess = int(guess)
            guesses_left -= 1
            
            if guess == current_floor:
                win.fill(WHITE)
                result_text = font_guess.render("Congratulations! You found the diamond!", True, BLACK)
                result_text2 = font_guess.render(f"It was on {current_floor}th floor", True, BLACK)            
                win.blit(result_text, (WIDTH/2 - result_text.get_width()/2, HEIGHT/2 - result_text.get_height()/2))
                win.blit(result_text2, (WIDTH/2 - result_text2.get_width()/2, HEIGHT/2 - result_text2.get_height()/2+30))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
        else:
            guesses_left -= 1

        if guesses_left == 0:
            game_over = True

# Start the game
game_loop()