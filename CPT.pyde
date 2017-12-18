play1 = False
play2 = False
play3 = False
menu = False
instructions = False
x_level1_background = 0
y_level1_background = 0
x_level2_background = 0
y_level2_background = 0
background1 = loadImage("background3.jpg")
background2 = loadImage("background4.jpg")
background3 = 0
level_1_loadingscreen = False
level_2_loadingscreen = False
level_3_loadingscreen = False
loading_time = 6
opacity = 255
fade_colour = 0
lives = 3
score = 0
y_speed = 10
laser_speed = 10
laser_damage = 5
player_size = 50
enemy_size = 40
enemy_speed = 3
enemy_hp = 10
boss_hp = 100
enemy_list = []
enemy_spawn = False
pos = PVector(0 + player_size / 2, 300)
laser_list = []
laser_center_list = []
key_up = False
key_down = False
key_space = False
click = False
hover_colour1 = [175, 238, 238]
hover_colour2 = [175, 238, 238]
hover_colour3 = [175, 238, 238]
hover_colour4 = [175, 238, 238]


def setup():
    global background1
    global background2
    global background3
    size(800, 600)
    background1 = loadImage("background3.jpg")
    background2 = loadImage("background4.jpg")


def draw():
    global play1
    global play2
    global menu
    global instructions
    global level_1_loadingscreen
    global level_2_loadingscreen
    global level_3_loadingscreen
    global loading_time
    global opacity
    global fade_colour
    global lives
    global score
    global speed
    global pos
    global laser_list
    global laser_center_list
    global key_up
    global key_down
    global key_space
    global laser_speed
    global laser_damage
    global hover_colour1
    global hover_colour2
    global hover_colour3
    global hover_colour4
    global click
    global enemy_size
    global enemy_speed
    global enemy_list
    global enemy_hp
    global enemy_spawn
    global boss_hp
    global x_level1_background
    global y_level1_background
    global x_level2_background
    global y_level2_background
    global background1
    global background2
    global background3
    img = loadImage("background.jpg")

    if menu == False:
        
        set(0, 0, img)
        textSize(48)
        strokeWeight(4)
        textAlign(CENTER, CENTER)
        fill(255)
        text("Airplane Shooting Game", width / 2, height / 2 - 50)

        fill(hover_colour1[0], hover_colour1[1], hover_colour1[2])
        rect(width - 110, height - 260, 68, 58)
        fill(hover_colour2[0], hover_colour2[1], hover_colour2[2])
        rect(width - 230, height - 190, 188, 58)
        fill(hover_colour3[0], hover_colour3[1], hover_colour3[2])
        rect(width - 112, height - 120, 68, 58)

        textSize(28)
        strokeWeight(2)
        textAlign(RIGHT, RIGHT)
        fill(0)
        text("Play", width - 50, height - 220)
        text("How To Play", width - 50, height - 150)
        text("Quit", width - 50, height - 80)

        center_play_square = PVector(width - 110 + 34, height - 260 + 29)
        center_howto_rect = PVector(width - 230 + 94, height - 190 + 29)
        center_quit_square = PVector(width - 112 + 34, height - 120 + 29)
        diff_play_sq = PVector(mouseX - center_play_square.x, mouseY - center_play_square.y)
        diff_howto_rect = PVector(mouseX - center_howto_rect.x, mouseY - center_howto_rect.y)
        diff_quit_sq = PVector(mouseX - center_quit_square.x, mouseY - center_quit_square.y)

        if diff_play_sq.x >= -34 and diff_play_sq.x <= 34 and diff_play_sq.y >= -29 and diff_play_sq.y <= 29:

            hover_colour1[0] = 0
            hover_colour1[1] = 206
            hover_colour1[2] = 209
            if click == True:
                level_1_loadingscreen = True
                menu = True

        if diff_play_sq.x <= -34 or diff_play_sq.x >= 34 or diff_play_sq.y <= -29 or diff_play_sq.y >= 29:

            hover_colour1[0] = 175
            hover_colour1[1] = 238
            hover_colour1[2] = 238

        if diff_howto_rect.x >= -94 and diff_howto_rect.x <= 94 and diff_howto_rect.y >= -29 and diff_howto_rect.y <= 29:

            hover_colour2[0] = 0
            hover_colour2[1] = 206
            hover_colour2[2] = 209
            if click == True:
                instructions = True

        if diff_howto_rect.x <= -94 or diff_howto_rect.x >= 94 or diff_howto_rect.y <= -29 or diff_howto_rect.y >= 29:

            hover_colour2[0] = 175
            hover_colour2[1] = 238
            hover_colour2[2] = 238

        if diff_quit_sq.x >= -34 and diff_quit_sq.x <= 34 and diff_quit_sq.y >= -29 and diff_quit_sq.y <= 29:

            hover_colour3[0] = 0
            hover_colour3[1] = 206
            hover_colour3[2] = 209
            if click == True:
                exit()

        if diff_quit_sq.x <= -34 or diff_quit_sq.x >= 34 or diff_quit_sq.y <= -29 or diff_quit_sq.y >= 29:

            hover_colour3[0] = 175
            hover_colour3[1] = 238
            hover_colour3[2] = 238

    if instructions == True:

        background(255)
        textSize(48)
        textAlign(CENTER, TOP)
        text("How To Play", width / 2, height / 2 - 250)
        textSize(24)
        textAlign(LEFT)

        text("Control your character with the arrow keys; UP and DOWN.", 65, 140)
        text("Use the Spacebar to shoot your weapon.", 65, 175)
        text("You have 3 lives, when you reach 0 lives, you lose.", 65, 210)
        text("Each level resets your lives to 3.", 65, 245)
        text("Each level has many enemies. There are 3 levels in total.", 65, 280)
        text("Each enemy defeated adds to your score.", 65, 315)
        text("Each level has a boss at the end. Defeating it clears the level.", 65, 350)

        fill(hover_colour4[0], hover_colour4[1], hover_colour4[2])
        rect(width - 760, height - 80, 70, 50)
        fill(0)
        text("Back", width - 750, height - 50)

        center_back_square = PVector(width - 760 + 35, height - 80 + 25)
        diff_back_sq = PVector(mouseX - center_back_square.x, mouseY - center_back_square.y)

        if diff_back_sq.x >= -35 and diff_back_sq.x <= 35 and diff_back_sq.y >= -25 and diff_back_sq.y <= 25:
            hover_colour4[0] = 0
            hover_colour4[1] = 206
            hover_colour4[2] = 209
            if click == True:
                instructions = False

        if diff_back_sq.x <= -35 or diff_back_sq.x >= 35 or diff_back_sq.y <= -25 or diff_back_sq.y >= 25:
            hover_colour4[0] = 175
            hover_colour4[1] = 238
            hover_colour4[2] = 238

    if level_1_loadingscreen == True:

        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 1", width / 2, height / 2)
        if frameCount % 5 == 0:
            loading_time -= 0.001
            opacity -= 255 / 20
            fade_colour += 255 / 20
            if fade_colour > 255:
                fade_colour = 255
                level_1_loadingscreen = False
                loading_time = 6
                opacity = 255
                fade_colour = 0
                play1 = True
            if loading_time == 0:
                level_1_loadingscreen = False
                loading_time = 6
                opacity = 255
                fade_colour = 0
                play1 = True

    if play1 == True:

        x_level1_background = constrain(x_level1_background, 0, background1.width - width)
        y_level1_background = constrain(y_level1_background, 0, background1.height - height)
        set(-x_level1_background, 0, background1)
        x_level1_background = frameCount

        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)

        fill(255, 0, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        if key_up == True:
            pos.y -= y_speed

        if key_down == True:
            pos.y += y_speed

        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed
            if lasers.x > width:
                laser_list.remove(lasers)
                
        if enemy_spawn == False:
            enemy_list.append(PVector(random(width + enemy_size/2, width + enemy_size*2), random(0 + enemy_size/2, height - enemy_size/2)))
            
        if len(enemy_list) > 10:
            enemy_spawn = True
            
        for enemies in enemy_list:
            fill(0)
            ellipse(enemies.x,enemies.y,enemy_size,enemy_size)
            enemies.x -= random(2,5)
            if enemies.x < 0:
                enemy_list.remove(enemies)
            if len(laser_list) > 0:
                temp = PVector(lasers.x + 13, lasers.y + 5)
                dif = PVector.sub(temp,enemies)
                if dif.mag() < enemy_size/2:
                    laser_list.remove(lasers)
                    enemy_list.remove(enemies)
                
        
        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

    if level_2_loadingscreen == True:

        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 2", width / 2, height / 2)
        if frameCount % 5 == 0:
            loading_time -= 0.001
            opacity -= 255 / 20
            fade_colour += 255 / 20
            if fade_colour > 255:
                fade_colour = 255
                level_2_loadingscreen = False
                loading_time = 6
                opacity = 255
                play2 = True
            if loading_time == 0:
                level_2_loadingscreen = False
                play2 = True
                fade_colour = 255
                loading_time = 6
                opacity = 6

    if play2 == True:

        x_level2_background = constrain(x_level2_background, 0, background2.width - width)
        y_level2_background = constrain(y_level2_background, 0, background2.height - height)
        set(-x_level2_background, 0, background2)
        x_level2_background = frameCount
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)

        fill(255, 0, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        if key_up == True:
            pos.y -= y_speed

        if key_down == True:
            pos.y += y_speed

        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed
            if lasers.x > width:
                laser_list.remove(lasers)

        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

    if level_3_loadingscreen == True:

        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 3", width / 2, height / 2)
        if frameCount % 5 == 0:
            loading_time -= 0.001
            opacity -= 255 / 20
            fade_colour += 255 / 20
            if fade_colour > 255:
                fade_colour = 255
                level_3_loadingscreen = False
                play3 = True
            if loading_time == 0:
                level_3_loadingscreen = False
                play3 = True


def mousePressed():
    global click
    if mouseButton == LEFT:
        click = True

def mouseReleased():
    global click
    if mouseButton == LEFT:
        click = False


def keyPressed():
    global key_up
    global key_down
    global key_space
    global laser_list
    if key == CODED:
        if keyCode == UP:
            key_up = True

    if key == CODED:
        if keyCode == DOWN:
            key_down = True

    if key == " ":
        key_space = True
        laser_list.append(PVector(pos.x + player_size / 2, pos.y))


def keyReleased():
    global key_up
    global key_down
    global key_space
    if key == CODED:
        if keyCode == UP:
            key_up = False

    if key == CODED:
        if keyCode == DOWN:
            key_down = False

    if key == " ":
        key_space = False
