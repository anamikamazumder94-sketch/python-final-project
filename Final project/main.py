import pygame
import random

# -----------------------------
# Pygame setup
# -----------------------------
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mario's Burger Quest")
clock = pygame.time.Clock()

# Background music
pygame.mixer.init()
pygame.mixer.music.load("Sounds/sound4.wav")
pygame.mixer.music.play(-1)

# -----------------------------
# Game variables
# -----------------------------
score = 0
lives = 5
speed = 5
level = 1
dt = 0

# Game states
game_state = "PLAYING"  # PLAYING, GAME_OVER, WIN

# Player
mario = pygame.image.load("Images/mario2-2.png")
mario_rect = mario.get_rect(center=(60, WINDOW_HEIGHT // 2))

# Foods
food = pygame.image.load("Images/burger 1.png")
taco = pygame.image.load("Images/tacos.png")

# Sounds
food_hit_sound = pygame.mixer.Sound("Sounds/food catch.wav")
food_miss_sound = pygame.mixer.Sound("Sounds/aww.mp3")
game_over_sound = pygame.mixer.Sound("Sounds/game over-2059.wav")

# Fonts
title_font = pygame.font.SysFont('impact', 40)
score_font = pygame.font.SysFont('impact', 25)
lives_font = pygame.font.SysFont('impact', 25)
game_over_font = pygame.font.SysFont('impact', 75)
restart_game_font = pygame.font.SysFont('impact', 30)

# Background
background = pygame.image.load("pic 1.jpg")
background = pygame.transform.scale(background, (800, 600))

# Texts
title_text = title_font.render("Mario's Burger Quest", True, (128, 0, 128))
# -----------------------------
    # HUD CALCULATIONS
    # -----------------------------
title_y = 20
score_y = title_y + title_text.get_height() + 5
HUD_HEIGHT = score_y + score_font.get_height() + 10
# -----------------------------
# Functions
# -----------------------------
def load_level(level):
    global burgers, tacos, lives
    burgers = []
    tacos = []

    if level == 1:
        for i in range(5):
            rect = food.get_rect()
            rect.x = WINDOW_WIDTH + random.randint(50, 400)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)
            burgers.append(rect)
    if level == 2:
        lives = 5  # reset lives for level 2
        for i in range(5):  # tacos = good
            rect = taco.get_rect()
            rect.x = WINDOW_WIDTH + random.randint(50, 500)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)
            tacos.append(rect)
        for i in range(3):  # burgers = dangerous
            rect = food.get_rect()
            rect.x = WINDOW_WIDTH + random.randint(100, 500)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)
            burgers.append(rect)

def show_welcome_screen():
    welcome_font = pygame.font.SysFont('impact', 50)  # smaller font
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to start
                    waiting = False

        screen.blit(background, (0, 0))

        # Render welcome text here with new font
        welcome_text = welcome_font.render("WELCOME TO MARIO'S BURGER QUEST", True, (180, 0, 250))  # cyan
        prompt_text = score_font.render("Press ENTER to Start", True, (0, 0, 0))
        
        # Center text
        welcome_rect = welcome_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        
        screen.blit(welcome_text, welcome_rect)
        screen.blit(prompt_text, prompt_rect)
        pygame.display.flip()
        clock.tick(60)   


def show_level_screen(level):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press ENTER to start level
                    waiting = False

        screen.blit(background, (0, 0))
        level_text = game_over_font.render(f"LEVEL {level}", True, (255, 255, 0))
        level_rect = level_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        screen.blit(level_text, level_rect)

        if level == 2:
            warning_text = score_font.render("Touch TACOS to score, avoid BURGERS!", True, (255, 0, 0))
            warning_rect = warning_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            screen.blit(warning_text, warning_rect)

        prompt_text = score_font.render("Press ENTER to Start", True, (255, 255, 255))
        prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80))
        screen.blit(prompt_text, prompt_rect)

        pygame.display.flip()
        clock.tick(60)

def show_restart_screen():
    screen.blit(background, (0, 0))
    lose_text = game_over_font.render("YOU LOSE!", True, (255, 0, 0))
    lose_rect = lose_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    screen.blit(lose_text, lose_rect)
    prompt_text = restart_game_font.render("Press ENTER to Restart", True, (255, 255, 0))
    prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    screen.blit(prompt_text, prompt_rect)
    pygame.display.flip()

def show_win_screen():
    screen.blit(background, (0, 0))
    win_text = game_over_font.render("YOU WIN!", True, (0, 255, 0))
    win_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    screen.blit(win_text, win_rect)
    prompt_text = restart_game_font.render("Press ENTER to Restart", True, (255, 255, 0))
    prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    screen.blit(prompt_text, prompt_rect)
    pygame.display.flip()
def show_level1_completed_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press ENTER to continue
                    waiting = False

        screen.blit(background, (0, 0))
        completed_text = game_over_font.render("LEVEL 1 COMPLETED!", True, (0, 255, 0))
        completed_rect = completed_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        screen.blit(completed_text, completed_rect)

        prompt_text = score_font.render("Press ENTER to continue to Level 2", True, (255, 255, 255))
        prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        screen.blit(prompt_text, prompt_rect)

        pygame.display.flip()
        clock.tick(60)

# Initialize level
show_welcome_screen()
load_level(level)
show_level_screen(level)
# -----------------------------
# Main loop
# -----------------------------
# Flags for screens
# -----------------------------
show_welcome = True
show_level_start = False
level1_completed = False
running = True
game_over_played = False
running = True
while running:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    

    # Draw Background + HUD
    screen.blit(background, (0, 0))
    screen.blit(title_text, (WINDOW_WIDTH//2 - title_text.get_width()//2, title_y))

    score_text = score_font.render(f"Score: {score}", True, (255, 255, 0))
    lives_text = lives_font.render(f"Lives: {max(lives,0)}", True, (255, 165, 0))  # Prevent negative display

    screen.blit(score_text, (10, score_y))
    screen.blit(lives_text, (WINDOW_WIDTH - lives_text.get_width() - 10, score_y))

    pygame.draw.line(screen, (0,0,255), (0,HUD_HEIGHT), (WINDOW_WIDTH,HUD_HEIGHT), 5)

    # -----------------------------
    # GAME OVER SCREEN
    # -----------------------------
    if game_state == "GAME_OVER":
        if not game_over_played:
            pygame.mixer.music.stop()
            game_over_sound.play()
            game_over_played = True

        show_restart_screen()

        if keys[pygame.K_RETURN]:
            # Reset
            game_state = "PLAYING"
            level = 1
            score = 0
            lives = 5
            mario_rect.center = (60, WINDOW_HEIGHT // 2)
            load_level(level)
            pygame.mixer.music.play(-1)
            game_over_played = False

        pygame.display.flip()
        continue

    # -----------------------------
    # WIN SCREEN
    # -----------------------------
    if game_state == "WIN":
        show_win_screen()

        if keys[pygame.K_RETURN]:
            # Reset
            game_state = "PLAYING"
            level = 1
            score = 0
            lives = 5
            mario_rect.center = (60, WINDOW_HEIGHT // 2)
            load_level(level)
            pygame.mixer.music.play(-1)

        pygame.display.flip()
        continue

    # -----------------------------
    # PLAYER MOVEMENT
    # -----------------------------
    if keys[pygame.K_UP] and mario_rect.y > HUD_HEIGHT + 5:
        mario_rect.y -= 300 * dt
    if keys[pygame.K_DOWN] and mario_rect.y < WINDOW_HEIGHT - mario.get_height() - 5:
        mario_rect.y += 300 * dt
    if keys[pygame.K_LEFT] and mario_rect.x > 0:
        mario_rect.x -= 300 * dt
    if keys[pygame.K_RIGHT] and mario_rect.x < WINDOW_WIDTH - mario.get_width():
        mario_rect.x += 300 * dt

    # -----------------------------
    # MOVE BURGERS
    # -----------------------------
    for rect in burgers:
        rect.x -= 200 * dt
        if rect.x < 0:
            rect.x = WINDOW_WIDTH + random.randint(50, 400)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

            if level == 1:
                lives -= 1
                if lives <= 0:
                    game_state = "GAME_OVER"

    # -----------------------------
    # MOVE TACOS
    # -----------------------------
    for rect in tacos:
        rect.x -= 230 * dt
        if rect.x < 0:
            rect.x = WINDOW_WIDTH + random.randint(50, 500)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

    # -----------------------------
    # DRAW MARIO + FOODS
    # -----------------------------
    screen.blit(mario, mario_rect)
    for rect in burgers:
        screen.blit(food, rect)
    for rect in tacos:
        screen.blit(taco, rect)

    # -----------------------------
    # COLLISION — LEVEL 1
    # -----------------------------
    if level == 1:
        for rect in burgers:
            if mario_rect.colliderect(rect):
                food_hit_sound.play()
                score += 1
                rect.x = WINDOW_WIDTH + random.randint(50,400)
                rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

        # LEVEL COMPLETED
        if score >= 10:
            show_level1_completed_screen()
            level = 2
            load_level(level)
            show_level_screen(level)

    # -----------------------------
    # COLLISION — LEVEL 2
    # -----------------------------
    if level == 2:
        for rect in tacos:
            if mario_rect.colliderect(rect):
                food_hit_sound.play()
                score += 1
                rect.x = WINDOW_WIDTH + random.randint(50,500)
                rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

        for rect in burgers:
            if mario_rect.colliderect(rect):
                food_miss_sound.play()
                lives -= 1
                rect.x = WINDOW_WIDTH + random.randint(50,500)
                rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

                if lives <= 0:
                    game_state = "GAME_OVER"

        if score >= 20:
            game_state = "WIN"

    pygame.display.flip()

pygame.quit()