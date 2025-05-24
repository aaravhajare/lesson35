import pygame as p
import math as m
import random as r

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

screen = p.display.set_mode((screen_w,screen_h))

background = p.image.load("background.png")

p.display.set_caption("Space Invaders")
icon = p.image.load("icon.png")
p.display.set_icon(icon)

# player

player = p.image.load("player.png")
player_x = p_start_x
player_y = p_start_y
player_x_change = 0

#enemy

enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
n_enemies = 6

for i in range(n_enemies):
    enemy.append(p.image.load("enemy.png"))
    enemy_x.append(r.randint(0, screen_w - 64))
    enemy_y.append(r.randint(e_start_y_min, e_start_y_max))
    enemy_x_change.append(e_speed_x)
    enemy_y_change.append(e_speed_y)

# bullet

bullet = p.image.loa("bullet.png")
bullet_x = 0
bullet_y = p_start_y
bullet_y_change = b_speed_y
bullet_x_change = 0
state = "ready"

#score
score_value = 0
font = p.font.Font("freesansbold.ttf",32)
text_x = 10
text_y = 10

def show_score(x,y):
    score = font.render("Score:" + str(score_value), True,(255,255,255))
    screen.blit(score, (x,y))

def game_over(x,y):
    over = font.render("Game Over" , True,(255,255,255))
    screen.blit(over, (x,y))

def player(x,y):
    screen.blit(player, (x,y))

def enemy(x,y,i):
    screen.blit(enemy[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = m.sqrt((m.pow((enemy_x - bullet_x), 2)) + (m.pow((enemy_y - bullet_y), 2)))
    if distance < colision_d:
        return True
    return False

