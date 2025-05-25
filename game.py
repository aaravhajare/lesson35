import pygame as p
import math as m
import random as r

# Game settings
screen_w = 800
screen_h = 600
p_start_x = 370
p_start_y = 380
e_start_y_min = 50
e_start_y_max = 150
e_speed_x = 4
e_speed_y = 40
b_speed_y = 10
colision_d = 30

p.init()
screen = p.display.set_mode((screen_w, screen_h))
background = p.image.load("background.png")
p.display.set_caption("Space Invaders")
icon = p.image.load("ufo.png")
p.display.set_icon(icon)

# Player
playerImg = p.image.load("player.png")
player_x = p_start_x
player_y = p_start_y
player_x_change = 0

# Enemy
enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
n_enemies = 6

for i in range(n_enemies):
    enemyImg.append(p.image.load("enemy.png"))
    enemy_x.append(r.randint(0, screen_w - 64))
    enemy_y.append(r.randint(e_start_y_min, e_start_y_max))
    enemy_x_change.append(e_speed_x)
    enemy_y_change.append(e_speed_y)

# Bullet
bullet = p.image.load("bullet.png")
bullet_x = 0
bullet_y = p_start_y
bullet_y_change = b_speed_y
state = "ready"

# Score
score_value = 0
font = p.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over(x, y):
    over = font.render("Game Over", True, (255, 255, 255))
    screen.blit(over, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global state
    state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = m.sqrt((m.pow((enemy_x - bullet_x), 2)) + (m.pow((enemy_y - bullet_y), 2)))
    return distance < colision_d

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        if event.type == p.KEYDOWN:
            if event.key == p.K_d:
                player_x_change = 5
            if event.key == p.K_a:
                player_x_change = -5
            if event.key == p.K_SPACE and state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        if event.type == p.KEYUP and event.key in (p.K_d, p.K_a):
            player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, screen_w - 64))

    for i in range(n_enemies):
        if enemy_y[i] > 340:
            for j in range(n_enemies):
                enemy_y[j] = 2000
            game_over(300, 250)
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_w - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = p_start_y
            state = "ready"
            score_value += 1
            enemy_x[i] = r.randint(0, screen_w - 64)
            enemy_y[i] = r.randint(e_start_y_min, e_start_y_max)

        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_y <= 0:
        bullet_y = p_start_y
        state = "ready"
    elif state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    p.display.update()
