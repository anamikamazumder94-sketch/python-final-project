import pygame
import random


# Pygame setup

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mario's Burger Quest")
clock = pygame.time.Clock()

# Background music
pygame.mixer.init()
pygame.mixer.music.load("Sounds/sound4.wav")
pygame.mixer.music.play(-1)


# Game variables

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

    # HUD CALCULATIONS
    
title_y = 20
score_y = title_y + title_text.get_height() + 5
HUD_HEIGHT = score_y + score_font.get_height() + 10

# Functions

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
def show_level3_screen():
    waiting = True
    font_big = pygame.font.SysFont("impact", 70)
    font_small = pygame.font.SysFont("impact", 25)  # smaller font for instructions
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # Check Play button
                if WINDOW_WIDTH//2 - 100 < mouse[0] < WINDOW_WIDTH//2 + 100 and WINDOW_HEIGHT//2 < mouse[1] < WINDOW_HEIGHT//2 + 50:
                    return "play"
                # Check Exit button
                if WINDOW_WIDTH//2 - 100 < mouse[0] < WINDOW_WIDTH//2 + 100 and WINDOW_HEIGHT//2 + 80 < mouse[1] < WINDOW_HEIGHT//2 + 130:
                    return "skip"

        screen.blit(background, (0, 0))

        title = font_big.render("Welcome to LEVEL 3", True, (255, 255, 0))
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
        screen.blit(title, title_rect)
                # Instruction text
        instruction_text = font_small.render("To jump press SPACE key", True, (255, 255, 255))
        instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 40))
        screen.blit(instruction_text, instruction_rect)

        # Draw buttons (no need for action return here)
        draw_button("Play Level 3", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2, 200, 50, (0,255,0), (0,200,0))
        draw_button("Exit", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 80, 200, 50, (255,0,0), (200,0,0))

        pygame.display.flip()
        clock.tick(60)
def draw_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()

    # Check if mouse is over button
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    # Draw text
    font = pygame.font.SysFont("impact", 30)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surf, text_rect)
def level3():
    import pygame, sys, random , math

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Level 3 - Mario Runner")

    # Ground
    GROUND_Y = 520

    # Colors
    YELLOW = (255, 215, 0)
    RED = (255, 0, 0)
    coin_sound = pygame.mixer.Sound("Sounds/sound5.wav")
    coin_channel = pygame.mixer.Channel(1)  # dedicate a channel for coin sound
    # Load Art
    MARIO_WIDTH, MARIO_HEIGHT = 48, 64
    MARIO_STAND = pygame.transform.scale(pygame.image.load("Super Mario.png"), (MARIO_WIDTH + 30, MARIO_HEIGHT))
    MARIO_JUMP = pygame.transform.scale(pygame.image.load("new Mario-2.png"), (MARIO_WIDTH, MARIO_HEIGHT))
    OBSTACLE_IMG = pygame.transform.scale(pygame.image.load("goomba.png"), (40, 50))
    BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
    COIN_IMG = pygame.transform.scale(pygame.image.load("coin.png"), (30, 30))
    mario_rect = MARIO_STAND.get_rect(midbottom=(100, GROUND_Y))
    velocity_y = 0
    gravity, jump_strength = 1200, -600
    is_jumping = False

    coins = []
    obstacles = []
    score = 0
    spawn_timer = 0
    OBSTACLE_INTERVAL = 2000

    font = pygame.font.SysFont("impact", 40)
    game_over = False
    win_score = 100

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if not game_over:

            # Jumping
            if keys[pygame.K_SPACE] and not is_jumping:
                velocity_y = jump_strength
                is_jumping = True

            velocity_y += gravity * dt
            mario_rect.y += velocity_y * dt

            # Floor check
            if mario_rect.bottom >= GROUND_Y:
                mario_rect.bottom = GROUND_Y
                is_jumping = False
                velocity_y = 0

            # Spawn objects
            spawn_timer += dt * 1000
            if spawn_timer >= OBSTACLE_INTERVAL:
                obs = OBSTACLE_IMG.get_rect(midbottom=(SCREEN_WIDTH + 50, GROUND_Y+5))
                obstacles.append(obs)

                # Spawn coins
                start_x = SCREEN_WIDTH + 200
                for i in range(5):
                    coin_rect = COIN_IMG.get_rect()
                    coin_rect.x = start_x + i * 60
                    coin_rect.y = GROUND_Y - 30 - random.randint(0, 50)
                    coins.append({
                        "rect": coin_rect,
                        "bounce": random.uniform(0, 3.14)  # phase for sine wave
                    })
                spawn_timer = 0

            for coin in coins[:]:
                # Move left
                coin["rect"].x -= 300 * dt

                # Remove if off-screen
                if coin["rect"].right < 0:
                    coins.remove(coin)
                    continue

                # Bounce effect for drawing
                bounce_height = 10
                coin["bounce"] += dt * 5  # speed of bouncing
                offset = bounce_height * math.sin(coin["bounce"])
                screen.blit(COIN_IMG, (coin["rect"].x, coin["rect"].y + offset))

                # Collision with Mario
                if mario_rect.colliderect(coin["rect"]):
                    score += 1
                    coins.remove(coin)
                    if not coin_channel.get_busy():
                        coin_channel.play(coin_sound)

            # Move obstacles
            for o in obstacles[:]:
                o.x -= 300 * dt
                if o.right < 0:
                    obstacles.remove(o)
                if mario_rect.colliderect(o):
                    game_over = True

            if score >= win_score:
                game_over = True

        # Drawing
        screen.blit(BG, (0, 0))

        for coin in coins:
    # Bounce effect
            bounce_height = 10  # pixels
            coin["bounce"] += dt * 5  # speed of bouncing
            offset = bounce_height * math.sin(coin["bounce"])
            coin_rect = coin["rect"]
            screen.blit(COIN_IMG, (coin_rect.x, coin_rect.y + offset))

        for o in obstacles:
            screen.blit(OBSTACLE_IMG, o)

        screen.blit(MARIO_JUMP if is_jumping else MARIO_STAND, mario_rect)

        score_text = font.render(f"Score: {score}", True, YELLOW)
        screen.blit(score_text, (10, 10))

        if game_over:
            coin_channel.stop()
            if score >= win_score:
                txt = "You Win!"
                result = "win"
            else:
                txt = "Game Over"
                result = "lose"

            msg = font.render(txt, True, RED)
            screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(2000)
            return result

        pygame.display.update()

# Initialize level
show_welcome_screen()
load_level(level)
show_level_screen(level)

# Main loop

# Flags for screens
level2_finished = False
level2_result = None
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

    
    # GAME OVER SCREEN
   
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
            level2_finished = False
            level2_result = None
        pygame.display.flip()
        continue

    
    # WIN SCREEN
 
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
            level2_finished = False
            level2_result = None
        pygame.display.flip()
        continue

  
    # PLAYER MOVEMENT
  
    if keys[pygame.K_UP] and mario_rect.y > HUD_HEIGHT + 5:
        mario_rect.y -= 300 * dt
    if keys[pygame.K_DOWN] and mario_rect.y < WINDOW_HEIGHT - mario.get_height() - 5:
        mario_rect.y += 300 * dt
    if keys[pygame.K_LEFT] and mario_rect.x > 0:
        mario_rect.x -= 300 * dt
    if keys[pygame.K_RIGHT] and mario_rect.x < WINDOW_WIDTH - mario.get_width():
        mario_rect.x += 300 * dt

    
    # MOVE BURGERS
   
    for rect in burgers:
        rect.x -= 200 * dt
        if rect.x < 0:
            rect.x = WINDOW_WIDTH + random.randint(50, 400)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

            if level == 1:
                lives -= 1
                if lives <= 0:
                    game_state = "GAME_OVER"

    
    # MOVE TACOS
   
    for rect in tacos:
        rect.x -= 230 * dt
        if rect.x < 0:
            rect.x = WINDOW_WIDTH + random.randint(50, 500)
            rect.y = random.randint(HUD_HEIGHT+5, WINDOW_HEIGHT - rect.height)

   
    # DRAW MARIO + FOODS
   
    screen.blit(mario, mario_rect)
    for rect in burgers:
        screen.blit(food, rect)
    for rect in tacos:
        screen.blit(taco, rect)

    
    # COLLISION — LEVEL 1
  
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

 
    
    # COLLISION — LEVEL 2


# LEVEL 2 COLLISIONS
    elif level == 2 and not level2_finished:
    # Collect tacos
        for rect in tacos:
            if mario_rect.colliderect(rect):
                food_hit_sound.play()
                score += 1
                rect.x = WINDOW_WIDTH + random.randint(50, 500)
                rect.y = random.randint(HUD_HEIGHT + 5, WINDOW_HEIGHT - rect.height)

        # Hit burgers
        for rect in burgers:
            if mario_rect.colliderect(rect):
                food_miss_sound.play()
                lives -= 1
                rect.x = WINDOW_WIDTH + random.randint(50, 500)
                rect.y = random.randint(HUD_HEIGHT + 5, WINDOW_HEIGHT - rect.height)

                if lives <= 0:
                    level2_finished = True
                    level2_result = "lose"

        # Level 2 win condition
        if score >= 20:
            level2_finished = True
            level2_result = "win"

    # --- AFTER LEVEL 2 FINISHES ---
    if level2_finished:
        pygame.mixer.music.stop()  # stop Level 2 music

        if level2_result == "lose":
            game_state = "GAME_OVER"  # show Game Over screen

        elif level2_result == "win":
            font = pygame.font.SysFont("impact", 75)
            screen.blit(background, (0, 0))
            txt = font.render("LEVEL 2 COMPLETED!", True, (0, 255, 0))
            screen.blit(txt, (WINDOW_WIDTH//2 - txt.get_width()//2, WINDOW_HEIGHT//2 - txt.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(1500)  # wait 1.5 seconds so player sees the message

            # Show Level 3 screen with buttons
            choice = show_level3_screen()  # player clicks button

            if choice == "skip":
                game_state = "GAME_OVER"  # player chose not to play Level 3

            elif choice == "play":
                # Start Level 3
                result = level3()  # runs Level 3 game

                if result == "win":
                    game_state = "WIN"
                else:
                    game_state = "GAME_OVER"  # after returning, show Game Over screen

    pygame.display.flip()
 # Main loop ends
pygame.quit()  # cleanly closes Pygame   