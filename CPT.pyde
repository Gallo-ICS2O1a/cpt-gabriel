screen = "menu"
frames = 0
x_level1_background = 0
y_level1_background = 0
x_level2_background = 0
y_level2_background = 0
background1 = loadImage("background3.jpg")
background2 = loadImage("background4.jpg")
background3 = 0
main_menu_background = loadImage("background.jpg")
powerup_scorepic = loadImage("powerup_score.gif")
powerup_heartpic = loadImage("powerup_heart.gif")
level_1_loadingscreen = False
level_2_loadingscreen = False
level_3_loadingscreen = False
loading_time = 6
opacity = 255
fade_colour = 0
lives = 5
lives_lost = 0
score = 0
y_speed = 5
laser_speed = 10
laser_damage = 5
last_shot = 0
player_size = 50
enemy_size = 40
enemy_speed = PVector(3,0)
enemy_kill_score = 50
boss_hp = 100
boss_size = 100
boss = PVector(800 + 100, 600/2)
boss_speed = PVector(2,0)
boss_attack = PVector(boss.x - boss_size/2,boss.y)
boss_attackspeed = PVector(0,0)
attacked = False
enemy_list = []
enemy_spawn = False
pos = PVector(0 + player_size / 2, 300)
laser_list = []
key_up = False
key_down = False
key_space = False
click = False
hover_colour1 = [175, 238, 238]
hover_colour2 = [175, 238, 238]
hover_colour3 = [175, 238, 238]
hover_colour4 = [175, 238, 238]
powerup_heart = PVector(random(800 + 100, 800 + 200),random(0, 600))
powerup_speed = PVector(random(2,4),0)
powerup_heart_spawn = False
powerup_heart_trigger = random(frames + 500, frames + 2000)
powerup_size = 45
powerup_scoremultiply_loc = PVector(random(800 + 100, 800 + 200),random(0, 600))
powerup_scoremultiply_trigger = random(frames + 200, frames + 3000)
powerup_scoremultiply = 2
powerup_scoremultiply_time = 20
powerup_scoremultiply_spawn = False
countdown = False

def retry_level1():
    
    #Retry function to reset level 1
    global pos
    global frames
    global laser_list
    global lives
    global x_level1_background
    global y_level1_background
    global enemy_list
    global screen
    global score
    global background1
    global lives_lost
    global last_shot
    global boss
    global boss_attack
    global boss_attackspeed
    
    background1 = loadImage("background3.jpg")
    pos = PVector(0 + player_size / 2, 300)
    laser_list = []
    lives = 5
    lives_lost -= 3
    x_level1_background = 0
    y_level1_background = 0
    frames = 0
    enemy_list = []
    score = 0
    screen = "level_1_loadingscreen"
    boss = PVector(800 + 100, 600/2)
    boss_attack = PVector(boss.x - boss_size/2,boss.y)
    boss_attackspeed = PVector(0,0)
    attacked = False
    
    
#def retry_level2():
    
#def retry_level3():
    
def powerup_scoremultiply_reset():
    
    global frames
    global powerup_scoremultiply_spawn
    global powerup_speed
    global powerup_scoremultiply_loc
    global powerup_scoremultiply_trigger
    
    powerup_speed = PVector(random(2,4),0)
    powerup_scoremultiply_loc = PVector(random(800 + 100, 800 + 200),random(0, 600))
    powerup_scoremultiply_trigger = powerup_scoremultiply_trigger = random(frames + 200, frames + 3000)
    powerup_scoremultiply_spawn = False
    
def powerup_heart_reset():
    
    global frames
    global powerup_heart_spawn
    global powerup_speed
    global powerup_heart
    global powerup_heart_trigger
    
    powerup_heart_spawn = False
    powerup_heart = PVector(random(800 + 100, 800 + 200),random(0, 600))
    powerup_speed = PVector(random(2,4),0)
    powerup_heart_trigger = random(frames + 500, frames + 2000)

def setup():
    
    #Loads the images (backgrounds) once
    #Sets the size of the window in which the game is played in to 800 x 600
    global background1
    global background2
    global background3
    global main_menu_background
    global powerup_scorepic
    global powerup_heartpic
    size(800, 600)
    background1 = loadImage("background3.jpg")
    background2 = loadImage("background4.jpg")
    main_menu_background = loadImage("background.jpg")
    powerup_scorepic = loadImage("powerup_score.gif")
    powerup_heartpic = loadImage("powerup_heart.gif")

def draw():
    global screen
    global loading_time
    global opacity
    global fade_colour
    global lives
    global lives_lost
    global score
    global y_speed
    global frames
    global pos
    global laser_list
    global key_up
    global key_down
    global key_space
    global laser_speed
    global laser_damage
    global last_shot
    global hover_colour1
    global hover_colour2
    global hover_colour3
    global hover_colour4
    global click
    global enemy_kill_score
    global enemy_size
    global enemy_speed
    global enemy_list
    global enemy_spawn
    global boss_hp
    global boss_size
    global boss
    global boss_speed
    global boss_attack
    global boss_attackspeed
    global x_level1_background
    global y_level1_background
    global x_level2_background
    global y_level2_background
    global background1
    global background2
    global background3
    global main_menu_background
    global enemy_spawntime
    global attacked
    global powerup_heart
    global powerup_speed
    global powerup_heart_spawn
    global powerup_heart_trigger
    global powerup_size
    global powerup_scoremultiply
    global powerup_scoremultiply_trigger
    global powerup_scoremultiply_time
    global powerup_scoremultiply_loc
    global powerup_scoremultiply_spawn
    global countdown
    global powerup_scorepic
    global powerup_heartpic
    
    #If the screen is on the menu screen (default), then do the following things
    if screen == "menu":
        
        #Calls the image used for the background of the main menu and sets it
        set(0, 0, main_menu_background)
        #Creates the Title 
        textSize(48)
        strokeWeight(4)
        textAlign(CENTER, CENTER)
        fill(255)
        text("Airplane Shooting Game", width / 2, height / 2 - 50)
        
        #Creates the rectangles which the menu options are in
        fill(hover_colour1[0], hover_colour1[1], hover_colour1[2])
        rect(width - 110, height - 260, 68, 58)
        fill(hover_colour2[0], hover_colour2[1], hover_colour2[2])
        rect(width - 230, height - 190, 188, 58)
        fill(hover_colour3[0], hover_colour3[1], hover_colour3[2])
        rect(width - 112, height - 120, 68, 58)
        
        #Menu options
        textSize(28)
        strokeWeight(2)
        textAlign(RIGHT, RIGHT)
        fill(0)
        text("Play", width - 50, height - 220)
        text("How To Play", width - 50, height - 150)
        text("Quit", width - 50, height - 80)
        
        #Finds the center of the rectangles created for the menu options
        center_play_square = PVector(width - 110 + 34, height - 260 + 29)
        center_howto_rect = PVector(width - 230 + 94, height - 190 + 29)
        center_quit_square = PVector(width - 112 + 34, height - 120 + 29)
        
        #Calculates the distance between the mouse and the center of the rectangles
        diff_play_sq = PVector(mouseX - center_play_square.x, mouseY - center_play_square.y)
        diff_howto_rect = PVector(mouseX - center_howto_rect.x, mouseY - center_howto_rect.y)
        diff_quit_sq = PVector(mouseX - center_quit_square.x, mouseY - center_quit_square.y)
        
        #Conditions for if the mouse is hovering over the rectangles, change their colours to let the player know which option they're hovering over
        if diff_play_sq.x >= -34 and diff_play_sq.x <= 34 and diff_play_sq.y >= -29 and diff_play_sq.y <= 29:

            hover_colour1[0] = 0
            hover_colour1[1] = 206
            hover_colour1[2] = 209
            
            #Checks if the player clicks a certain option; in this case if the play button is clicked, then the first level begins
            if click == True:
                screen = "level_1_loadingscreen"

        if diff_play_sq.x <= -34 or diff_play_sq.x >= 34 or diff_play_sq.y <= -29 or diff_play_sq.y >= 29:

            hover_colour1[0] = 175
            hover_colour1[1] = 238
            hover_colour1[2] = 238

        if diff_howto_rect.x >= -94 and diff_howto_rect.x <= 94 and diff_howto_rect.y >= -29 and diff_howto_rect.y <= 29:

            hover_colour2[0] = 0
            hover_colour2[1] = 206
            hover_colour2[2] = 209
            
            #Checks if the player clicks the instructions, if so, directs them to the instructions screen 
            if click == True:
                screen = "instructions"

        if diff_howto_rect.x <= -94 or diff_howto_rect.x >= 94 or diff_howto_rect.y <= -29 or diff_howto_rect.y >= 29:

            hover_colour2[0] = 175
            hover_colour2[1] = 238
            hover_colour2[2] = 238

        if diff_quit_sq.x >= -34 and diff_quit_sq.x <= 34 and diff_quit_sq.y >= -29 and diff_quit_sq.y <= 29:

            hover_colour3[0] = 0
            hover_colour3[1] = 206
            hover_colour3[2] = 209
            
            #Checks if the player clicked exit, if so, exits the game
            if click == True:
                exit()

        if diff_quit_sq.x <= -34 or diff_quit_sq.x >= 34 or diff_quit_sq.y <= -29 or diff_quit_sq.y >= 29:

            hover_colour3[0] = 175
            hover_colour3[1] = 238
            hover_colour3[2] = 238

    #If the screen is on instructions, do the following things
    if screen == "instructions":

        #Creates the background for the instruction menu
        background(255)
        
        #Creates the title
        textSize(48)
        textAlign(CENTER, TOP)
        text("How To Play", width / 2, height / 2 - 250)
        
        #How to play rules
        textSize(24)
        textAlign(LEFT)

        text("Control your character with the arrow keys; UP and DOWN.", 65, 140)
        text("Use the Spacebar to shoot your weapon.", 65, 175)
        text("You have 3 lives, when you reach 0 lives, you lose.", 65, 210)
        text("Each level resets your lives to 3.", 65, 245)
        text("Each level has many enemies. There are 3 levels in total.", 65, 280)
        text("Each enemy defeated adds to your score.", 65, 315)
        text("Each level has a boss at the end. Defeating it clears the level.", 65, 350)
        
        #Creates the "back" button to return to the main menu
        fill(hover_colour4[0], hover_colour4[1], hover_colour4[2])
        rect(width - 760, height - 80, 70, 50)
        fill(0)
        text("Back", width - 750, height - 50)

        #Finds the center of the back button
        center_back_square = PVector(width - 760 + 35, height - 80 + 25)
        
        #Finds the difference between the center of the back button and the player's mouse
        diff_back_sq = PVector(mouseX - center_back_square.x, mouseY - center_back_square.y)

        #Conditions for checking if the mouse is hovering over the back button; if it is, change the colour
        if diff_back_sq.x >= -35 and diff_back_sq.x <= 35 and diff_back_sq.y >= -25 and diff_back_sq.y <= 25:
            hover_colour4[0] = 0
            hover_colour4[1] = 206
            hover_colour4[2] = 209
            
            #If the mouse is hovering over the back button and it is clicked, then return to the menu by setting the screen variable to menu
            if click == True:
                screen = "menu"

        if diff_back_sq.x <= -35 or diff_back_sq.x >= 35 or diff_back_sq.y <= -25 or diff_back_sq.y >= 25:
            hover_colour4[0] = 175
            hover_colour4[1] = 238
            hover_colour4[2] = 238
    
    #Checks if the screen variable is equal to the loading screen for level 1
    #If it is, then do the following things
    if screen == "level_1_loadingscreen":
        
        #Creates the background for the level 1 loading screen
        background(fade_colour, opacity)
        fill(255, 0, 0, opacity) 
        
        #Creates the "Level 1" text in the middle of the screen
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 1", width / 2, height / 2)
        
        #Creates the fadeaway effect for the "Level 1" text
        #Every 5 frames, reduces the opacity of the text by 255/20,
        #Increase the fade_colour variable by 255/20, causing the background colour to change until it reaches 255 (black)
        if frames % 5 == 0:
            opacity -= 255 / 20
            fade_colour += 255 / 20
            
            #If the fade_colour variable's value is greater than 255 (black colour), set it to black (255) and change the screen to the first level
            #When the screen becomes black, it means the fadeaway effect is done, thus the variables used are reset to be used again
            if fade_colour > 255:
                fade_colour = 255
                opacity = 255
                fade_colour = 0
                screen = "level1"
    
    #Checks if the screen variable is equal to level1,
    #If it is, do the following things
    if screen == "level1":
       
        time = millis() 
        #Creates the moving background (scrolling background)
        x_level1_background = constrain(x_level1_background, 0, background1.width - width)
        y_level1_background = constrain(y_level1_background, 0, background1.height - height)
        set(-x_level1_background, 0, background1)
        x_level1_background = frames
        powerup_scorepic.resize(powerup_size,powerup_size)
        powerup_heartpic.resize(powerup_size,powerup_size)
        
        #Score and lives text on the bottom of the screen
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)
        text("Score: " + str(score), width - 770, height - 30)
        
        #Creates the player
        fill(255, 0, 0)
        ellipse(pos.x, pos.y, player_size, player_size)
    
        
        
        #Checks if the up or down arrow keys are pressed and moves the player in the corresponding directon
        if key_up == True:
            pos.y -= y_speed

        if key_down == True:
            pos.y += y_speed
            
        #Creates the lasers
        #Loops through the laser_list and draws them (according to their location)
        #They also have their own speed variable so they move from left to right
        if key_space == True:
            if time >= last_shot + 500:
                laser_list.append(PVector(pos.x + player_size / 2, pos.y))
                last_shot = time
                key_space = False

       
        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed
            
            #If the lasers reach the end of the screen, removes the laser location from the list
            if lasers.x > width:
                laser_list.remove(lasers)
                
            
        #If the enemy_spawn variable is set to false, create enemies and add their randomized spawn location to the list of enemies        
        if enemy_spawn == False:
            enemy_list.append(PVector(random(width + enemy_size/2, width + enemy_size*5), random(0 + enemy_size/2, height - enemy_size/2)))
            
        # Checks the length of the enemy_list
        # If it's greater than 10 stop the spawning of enemies,
        # by setting the enemy_spawn variable to true
        # Every 40 frames, spawn more enemies
        # by setting the enemy_spawn variable to false

        if len(enemy_list) > 10:
            enemy_spawn = True

        if frames % 40 == 0:
            enemy_spawn = False

        # Creates the enemies
        # Loops through the list of enemies
        # and spawns them based on their location stored in the list
        # They have their own independent speed
        # Go from right to left (spawns on the right side of the screen)
        for enemy in enemy_list:
            fill(0)
            ellipse(enemy.x, enemy.y, enemy_size, enemy_size)
            enemy.x -= enemy_speed.x

            # If the enemies go past the left side of the screen,
            # remove them from the enemy list
            if enemy.x < 0:
                enemy_list.remove(enemy)

            # Collision Detection
            # If an enemy hits the player,
            # the number of lives will decrease by 1
            # and the enemy will be removed
            dif_playerhit = PVector.sub(enemy, pos)
            if dif_playerhit.mag() < player_size/2 + enemy_size/2:
                enemy_list.remove(enemy)
                lives -= 1
                lives_lost += 1

            # Loops through the laser_list
            # Finds the centre of the lasers
            # and the difference between the centre of the laser
            # and the centre of the enemies
            for lasers in laser_list:
                centre_enemylaser = PVector(lasers.x + 13, lasers.y + 5)
                dif = PVector.sub(centre_enemylaser, enemy)

                # Checks if the laser hits an enemy
                # If the distance between the laser
                # and the enemy is less than the radius of the enemy,
                # Remove the laser, remove the enemy,
                # and increase the score by 50 points.
                if dif.mag() < enemy_size/2:
                    enemy_list.remove(enemy)
                    laser_list.remove(lasers)
                    if countdown is True:
                        score += enemy_kill_score * powerup_scoremultiply
                    else:
                        score += enemy_kill_score
                    break

        fill(255, 0, 0)
        if frames >= powerup_heart_trigger:
            image(powerup_heartpic,powerup_heart.x,powerup_heart.y)
            powerup_heart_spawn = True

        if powerup_heart_spawn is True:
            powerup_heart.sub(powerup_speed)

        if powerup_heart.x < 0:
            powerup_heart_reset()

        powerup_heart_dif = PVector.sub(pos, powerup_heart)
        if powerup_heart_dif.mag() < player_size/2 + powerup_size/2:
            if lives == 5:
                score += 200
            else:
                lives += 1
            powerup_heart_reset()

        fill(0, 0, 255)
        if frames >= powerup_scoremultiply_trigger:
            image(powerup_scorepic,powerup_scoremultiply_loc.x,powerup_scoremultiply_loc.y)
            powerup_scoremultiply_spawn = True

        if powerup_scoremultiply_spawn is True:
            powerup_scoremultiply_loc.sub(powerup_speed)

        if powerup_scoremultiply_loc.x < 0:
            powerup_scoremultiply_reset()

        powerup_score_dif = PVector.sub(pos, powerup_scoremultiply_loc)
        if powerup_score_dif.mag() < player_size/2 + powerup_size/2:
            countdown = True
            powerup_scoremultiply_reset()
            print(powerup_scoremultiply_time)

        if countdown is True:
            fill(255)
            textSize(30)
            textAlign(BOTTOM, CENTER)
            text("x2 Score Time :" + str(powerup_scoremultiply_time),
                 width/2 - 120, height - 45)
            if frames % 60 == 0:
                powerup_scoremultiply_time -= 1
                if powerup_scoremultiply_time == 0:
                    powerup_scoremultiply_time = 20
                    countdown = False

        # If the frame count is greater than the scrolling picture's background
        # Subtracted by the game window width (boss area),
        # Do the following things
        if frames > background1.width - width:

            # Stops Spawning Enemies
            enemy_spawn = True

            # Creates the Boss
            fill(255)
            ellipse(boss.x, boss.y, boss_size, boss_size)

            fill(255)
            textSize(24)
            text("Boss HP: " + str(boss_hp), boss.x - boss_size/2 - 13,
                 boss.y + boss_size/2 + 25)

            # Boss Speed
            boss.x -= boss_speed.x
            if boss.x <= width - 100:
                boss_speed.x = 0

            if attacked is False:
                boss_dif = PVector.sub(boss_attack, pos)
                push = PVector.fromAngle(boss_dif.heading())
                push.mult(random(5, 8))
                boss_attackspeed = PVector(0, 0)
                boss_attackspeed.add(push)
                attacked = True

            ellipse(boss_attack.x, boss_attack.y, 20, 20)
            boss_attack.sub(boss_attackspeed)
            boss_hitplayer = PVector.sub(boss_attack, pos)

            if boss_hitplayer.mag() < player_size/2:
                lives -= 1
                lives_lost += 1
                boss_attack.x = boss.x
                boss_attack.y = height/2
                attacked = False

            if boss_attack.x < 0:
                boss_attack.x = boss.x
                boss_attack.y = height/2
                attacked = False

            for lasers in laser_list:
                centre_bosslaser = PVector(lasers.x + 13, lasers.y + 5)
                boss_dif = PVector.sub(centre_bosslaser, boss)
                if boss_dif.mag() < boss_size/2:
                    laser_list.remove(lasers)
                    boss_hp -= 5
                    break
            
            if boss_hp <= 0:
                score += 500
                boss.y += 2
                boss_attackspeed = PVector(0, 0)
                boss_attack = PVector(width + 100, height + 100)
                attacked = True
                
        if lives == 0:
            screen = "gameover1"

        if screen == "gameover1":
            background(255)
            textSize(48)
            fill(0)
            textAlign(CENTER, CENTER)
            text("GAME OVER!", width/2, height/2)
            textSize(30)
            fill(0, 255, 0)
            text("Press Space To Play Again", width/2, height/2 + 50)

        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

    if screen == "level_2_loadingscreen":

        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 2", width / 2, height / 2)
        if frames % 5 == 0:
            loading_time -= 0.001
            opacity -= 255 / 20
            fade_colour += 255 / 20
            if fade_colour > 255:
                fade_colour = 255
                loading_time = 6
                opacity = 255
                screen = "level2"
            if loading_time == 0:
                screen = "level2"
                fade_colour = 255
                loading_time = 6
                opacity = 6

    if screen == "level2":

        x_level2_background = constrain(x_level2_background, 0,
                                        background2.width - width)
        y_level2_background = constrain(y_level2_background, 0,
                                        background2.height - height)
        set(-x_level2_background, 0, background2)
        x_level2_background = frames
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)

        fill(255, 0, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        if key_up is True:
            pos.y -= y_speed

        if key_down is True:
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

    if screen == "level_3_loadingscreen":

        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 3", width / 2, height / 2)
        if frames % 5 == 0:
            loading_time -= 0.001
            opacity -= 255 / 20
            fade_colour += 255 / 20
            if fade_colour > 255:
                fade_colour = 255
                screen = "level3"
            if loading_time == 0:
                screen = "level3"

    frames += 1


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
    global last_shot
    if key == CODED:
        if keyCode == UP:
            key_up = True
        elif keyCode == DOWN:
            key_down = True

    if key == " ":
        key_space = True

        if screen == "gameover1":
            retry_level1()
        if screen == "gameover2":
            retry_level2()
        if screen == "gameover3":
            retry_level3()


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
