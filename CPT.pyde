screen = "menu"
frames = 0
colour1 = 255
colour2 = 255
colour3 = 255
x_level1_background = 0
y_level1_background = 0
x_level2_background = 0
y_level2_background = 0
x_level3_background = 0
y_level3_background = 0
main_menu_background = loadImage("background.jpg")
background1 = loadImage("background1.jpg")
background2 = loadImage("background2.jpg")
background3 = loadImage("background3.jpg")
powerup_scorepic = loadImage("powerup_score.gif")
powerup_heartpic = loadImage("powerup_heart.gif")
giantLaserpic = loadImage("giant_laser.gif")
level_1_loadingscreen = False
level_2_loadingscreen = False
level_3_loadingscreen = False
loading_time = 6
opacity = 255
fade_colour = 0
lives = 5
lives_lost = 0
score = 0
total_score = 0
bonus = 0
y_speed = 5
laser_speed = 10
laser_damage = 5
last_shot = 0
player_size = 50
enemy_list = []
enemy_spawn = False
enemy_size = 40
enemy_speed = PVector(3, 0)
enemy_kill_score = 50
boss_hp = 100
boss_size = 100
boss_loc = PVector(800 + 100, 600/2)
boss_speed = PVector(2, 0)
boss_attack = PVector(boss_loc.x, boss_loc.y)
boss_attackspeed = PVector(0, 0)
attacked = False
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
powerup_heart_loc = PVector(random(800 + 100, 800 + 200),
                            random(0, 600))
powerup_speed = PVector(random(2, 4), 0)
powerup_heart_spawn = False
powerup_heart_trigger = random(frames + 500, frames + 2000)
powerup_size = 45
powerup_scoremultiply_loc = PVector(random(800 + 100, 800 + 200),
                                    random(0, 600))
powerup_scoremultiply_trigger = random(frames + 200, frames + 3000)
powerup_scoremultiply = 2
powerup_scoremultiply_time = 20
powerup_scoremultiply_spawn = False
countdown = False
giantLasertrigger = random(frames + 600, 1200)
warningcolour = 255
passedLasertrigger = 0
randomLaserOccurence = None
giantLaser_loc = -800
giantLaser_yspeed = 5
giantLaserstopmove = False
done_moving = 0
warningsign = False
angle = 0


def gameover():
    # Creates the gameover screen
    background(255)
    textSize(48)
    fill(0)
    textAlign(CENTER, CENTER)
    text("GAME OVER!", width/2, height/2)
    textSize(30)
    fill(0, 255, 0)
    text("Press Space To Play Again", width/2, height/2 + 50)


def bossDead():
    # Actions to do when the boss is dead
    global score
    global total_score
    global boss_attackspeed
    global boss_attack
    global attacked
    global boss_hp

    score += 500
    total_score += score
    boss_attackspeed = PVector(0, 0)
    boss_attack = PVector(width + 100, height + 100)
    attacked = True
    boss_hp = -1


def giantLaser():
    # Determines whether the random occurence will happen
    # If true, a giant laser randomly spawns to help the player
    num = random(1)
    return num >= 0.7


def reset_level():

    # Retry function to reset the level
    # Used for both retries and transitions between levels
    global pos
    global frames
    global laser_list, laser_damage
    global enemy_list
    global lives
    global x_level1_background, y_level1_background, background1
    global x_level2_background, y_level2_background, background2
    global x_level3_background, y_level3_background, background3
    global screen
    global score
    global last_shot
    global boss_hp, boss_loc, boss_attack, boss_attackspeed
    global boss_speed, attacked
    global countdown
    global powerup_heart_loc, powerup_speed
    global powerup_heart_loc_spawn, powerup_heart_trigger
    global powerup_scoremultiply_loc, powerup_scoremultiply_trigger
    global powerup_scoremultiply_time, powerup_scoremultiply_spawn
    global giantLasertrigger, warningcolour, passedLasertrigger
    global randomLaserOccurence, giantLaser_loc, giantLaser_yspeed
    global giantLaserstopmove, done_moving, warningsign

    pos = PVector(0 + player_size / 2, 300)
    laser_list = []
    laser_damage = 5
    lives = 5
    frames = 0
    enemy_list = []
    score = 0
    powerup_heart_loc = PVector(random(800 + 100, 800 + 200),
                                random(0, 600))
    powerup_speed = PVector(random(2, 4), 0)
    powerup_heart_loc_spawn = False
    powerup_heart_trigger = random(frames + 500, frames + 2000)
    powerup_scoremultiply_loc = PVector(random(800 + 100, 800 + 200),
                                        random(0, 600))
    powerup_scoremultiply_trigger = random(frames + 200, frames + 3000)
    powerup_scoremultiply_time = 20
    powerup_scoremultiply_spawn = False
    countdown = False
    boss_hp = 100
    boss_loc = PVector(800 + 100, 600/2)
    boss_attack = PVector(boss_loc.x - boss_size/2, boss_loc.y)
    boss_attackspeed = PVector(0, 0)
    boss_speed = PVector(2, 0)
    attacked = False
    giantLasertrigger = random(frames + 300, 1000)
    warningcolour = 255
    passedLasertrigger = 0
    randomLaserOccurence = giantLaser()
    giantLaser_loc = -800
    giantLaser_yspeed = 5
    giantLaserstopmove = False
    warningsign = False
    done_moving = 0

    if screen == 'gameover1':
        background1 = loadImage("background1.jpg")
        x_level1_background = 0
        y_level1_background = 0
        screen = "level_1_loadingscreen"

    if screen == 'gameover2':
        background2 = loadImage("background2.jpg")
        x_level2_background = 0
        y_level2_background = 0
        screen = 'level_2_loadingscreen'

    if screen == 'gameover3':
        background3 = loadImage("background3.jpg")
        x_level3_background = 0
        y_level3_background = 0
        screen = 'level_3_loadingscreen'


def powerup_scoremultiply_reset():

    # Function to reset the scoremultiplier powerup

    global frames
    global powerup_scoremultiply_spawn
    global powerup_speed
    global powerup_scoremultiply_loc
    global powerup_scoremultiply_trigger

    powerup_speed = PVector(random(2, 4), 0)
    powerup_scoremultiply_loc = PVector(random(800 + 100, 800 + 200),
                                        random(0, 600))
    powerup_scoremultiply_trigger = random(frames + 200, frames + 3000)
    powerup_scoremultiply_spawn = False


def powerup_heart_reset():

    # Function to reset the heart powerup

    global frames
    global powerup_heart_spawn
    global powerup_speed
    global powerup_heart_loc
    global powerup_heart_trigger

    powerup_heart_spawn = False
    powerup_heart_loc = PVector(random(800 + 100, 800 + 200), random(0, 600))
    powerup_speed = PVector(random(2, 4), 0)
    powerup_heart_trigger = random(frames + 500, frames + 2000)


def setup():

    # Loads the backgrounds and images
    # Sets the size of the window in which the game is played in, to 800 x 600
    # Sets the temp variable to the returned boolean of the giantLaser function
    global background1
    global background2
    global background3
    global main_menu_background
    global powerup_scorepic
    global powerup_heartpic
    global giantLaserpic
    global randomLaserOccurence
    size(800, 600)
    background1 = loadImage("background1.jpg")
    background2 = loadImage("background2.jpg")
    background3 = loadImage("background3.jpg")
    main_menu_background = loadImage("background.jpg")
    powerup_scorepic = loadImage("powerup_score.gif")
    powerup_heartpic = loadImage("powerup_heart.gif")
    giantLaserpic = loadImage("giant_laser.gif")
    randomLaserOccurence = giantLaser()


def draw():
    global screen
    global frames
    global loading_time
    global opacity
    global fade_colour
    global lives, lives_lost
    global score, total_score
    global pos, y_speed
    global laser_list, laser_speed, laser_damage, last_shot
    global key_up, key_down, key_space
    global hover_colour1, hover_colour2, hover_colour3, hover_colour4
    global click
    global enemy_list, enemy_kill_score, enemy_size, enemy_speed, enemy_spawn
    global main_menu_background
    global boss_loc, boss_hp, boss_size, boss_speed
    global boss_attack, boss_attackspeed, attacked
    global background1, x_level1_background, y_level1_background
    global background2, x_level2_background, y_level2_background
    global background3, x_level3_background, y_level3_background
    global powerup_size, powerup_speed
    global powerup_heart_loc, powerup_heart_spawn
    global powerup_heart_trigger, powerup_heartpic
    global powerup_scoremultiply_loc, powerup_scoremultiply
    global powerup_scoremultiply_trigger, powerup_scoremultiply_time
    global powerup_scoremultiply_spawn, countdown, powerup_scorepic
    global giantLasertrigger, warningcolour, passedLasertrigger
    global randomLaserOccurence, giantLaserpic, giantLaser_loc
    global giantLaser_yspeed, giantLaserstopmove, done_moving, warningsign
    global angle
    global colour1, colour2, colour3
    global bonus

    # If the screen is on the menu screen (default)
    # then do the following things
    if screen == "menu":

        # Calls the image used for the background of the main menu and sets it
        set(0, 0, main_menu_background)
        # Creates the Title
        textSize(48)
        strokeWeight(4)
        textAlign(CENTER, CENTER)
        fill(255)
        text("Space Shooting Game", width / 2, height / 2 - 50)

        # Creates the rectangles which the menu options are in
        fill(hover_colour1[0], hover_colour1[1], hover_colour1[2])
        rect(width - 110, height - 260, 68, 58)
        fill(hover_colour2[0], hover_colour2[1], hover_colour2[2])
        rect(width - 230, height - 190, 188, 58)
        fill(hover_colour3[0], hover_colour3[1], hover_colour3[2])
        rect(width - 112, height - 120, 68, 58)

        # Menu options
        textSize(28)
        strokeWeight(2)
        textAlign(RIGHT, RIGHT)
        fill(0)
        text("Play", width - 50, height - 220)
        text("How To Play", width - 50, height - 150)
        text("Quit", width - 50, height - 80)

        # Finds the center of the rectangles created for the menu options
        center_play_square = PVector(width - 110 + 34, height - 260 + 29)
        center_howto_rect = PVector(width - 230 + 94, height - 190 + 29)
        center_quit_square = PVector(width - 112 + 34, height - 120 + 29)

        # Calculates the distance between the mouse
        # and the center of the rectangles
        diff_play_sq = PVector(mouseX - center_play_square.x,
                               mouseY - center_play_square.y)
        diff_howto_rect = PVector(mouseX - center_howto_rect.x,
                                  mouseY - center_howto_rect.y)
        diff_quit_sq = PVector(mouseX - center_quit_square.x,
                               mouseY - center_quit_square.y)

        # Conditions for if the mouse is hovering over the rectangles
        # Change their colours to let the player
        # know which option they're hovering over

        if (diff_play_sq.x >= -34 and diff_play_sq.x <= 34 and
           diff_play_sq.y >= -29 and diff_play_sq.y <= 29):

            hover_colour1[0] = 0
            hover_colour1[1] = 206
            hover_colour1[2] = 209

            # Checks if the player clicks a certain option;
            # in this case if the play button is clicked,
            # then the first level begins
            if click is True:
                screen = "level_1_loadingscreen"

        if (diff_play_sq.x <= -34 or diff_play_sq.x >= 34 or
           diff_play_sq.y <= -29 or diff_play_sq.y >= 29):

            hover_colour1[0] = 175
            hover_colour1[1] = 238
            hover_colour1[2] = 238

        if (diff_howto_rect.x >= -94 and diff_howto_rect.x <= 94 and
           diff_howto_rect.y >= -29 and diff_howto_rect.y <= 29):

            hover_colour2[0] = 0
            hover_colour2[1] = 206
            hover_colour2[2] = 209

            # Checks if the player clicks the how to play button,
            # if so, directs them to the instructions screen
            if click is True:
                screen = "instructions"

        if (diff_howto_rect.x <= -94 or diff_howto_rect.x >= 94 or
           diff_howto_rect.y <= -29 or diff_howto_rect.y >= 29):

            hover_colour2[0] = 175
            hover_colour2[1] = 238
            hover_colour2[2] = 238

        if (diff_quit_sq.x >= -34 and diff_quit_sq.x <= 34 and
           diff_quit_sq.y >= -29 and diff_quit_sq.y <= 29):

            hover_colour3[0] = 0
            hover_colour3[1] = 206
            hover_colour3[2] = 209

            # Checks if the player clicked exit, if so, exits the game
            if click is True:
                exit()

        if (diff_quit_sq.x <= -34 or diff_quit_sq.x >= 34 or
           diff_quit_sq.y <= -29 or diff_quit_sq.y >= 29):

            hover_colour3[0] = 175
            hover_colour3[1] = 238
            hover_colour3[2] = 238

    # If the screen is on instructions, do the following things
    if screen == "instructions":

        # Creates the background for the instruction menu
        background(255)

        # Creates the title
        textSize(48)
        textAlign(CENTER, TOP)
        text("How To Play", width / 2, height / 2 - 300)

        # How to play
        textSize(18)
        textAlign(LEFT)

        text("You are the yellow ellipse.", 65, 90)
        text("Control your character using the "
             "UP and DOWN arrow keys.", 65, 120)
        text("Shoot with the spacebar.", 65, 150)
        text("Your goal is to defeat as many enemies as you can.", 65, 180)
        text("and defeat the boss at the end of that level.", 65, 210)
        text("You have 5 lives, when you reach 0 lives, "
             "you can retry", 65, 240)
        text("You lose a life when you get hit by an enemy or boss.", 65, 270)
        text("Each life lost is counted, even after a retry.", 65, 300)
        text("You will recieve a bonus to your score "
             "depending on how many lives were lost.", 65, 330)
        text("Each level resets your lives to 5.", 65, 360)
        text("There are 3 levels in total.", 65, 390)
        text("Each enemy defeated adds to your score.", 65, 420)
        text("Defeating the boss clears the level and "
             "grants an extra score bonus.", 65, 450)
        text("There are also powerups with different effects.", 65, 480)

        pushMatrix()
        imageMode(CENTER)
        translate(730, 80)
        powerup_scorepic.resize(powerup_size, powerup_size)
        rotate(radians(angle))
        image(powerup_scorepic, 0, 0)
        popMatrix()

        angle += 5

        # Creates the "back" button to return to the main menu
        textSize(28)
        fill(hover_colour4[0], hover_colour4[1], hover_colour4[2])
        rect(width - 760, height - 70, 70, 50)
        fill(0)
        text("Back", width - 755, height - 37)

        # Finds the center of the back button
        center_back_square = PVector(width - 760 + 35, height - 45)

        # Finds the difference between the
        # center of the back button and the player's mouse
        diff_back_sq = PVector(mouseX - center_back_square.x,
                               mouseY - center_back_square.y)

        # Conditions for checking if the mouse is hovering over the back button
        # if it is, change the colour
        if (diff_back_sq.x >= -35 and diff_back_sq.x <= 35 and
           diff_back_sq.y >= -25 and diff_back_sq.y <= 25):
            hover_colour4[0] = 0
            hover_colour4[1] = 206
            hover_colour4[2] = 209

            # If the mouse is hovering over the back button and
            # it is clicked, then return to the menu by
            # setting the screen variable to menu
            if click is True:
                screen = "menu"

        if (diff_back_sq.x <= -35 or diff_back_sq.x >= 35 or
           diff_back_sq.y <= -25 or diff_back_sq.y >= 25):
            hover_colour4[0] = 175
            hover_colour4[1] = 238
            hover_colour4[2] = 238

    # Checks if the screen variable is equal to the loading screen for level 1
    # If it is, then do the following things
    if screen == "level_1_loadingscreen":

        # Creates the background for the level 1 loading screen
        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)

        # Creates the "Level 1" text in the middle of the screen
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 1", width / 2, height / 2)

        # Creates the fadeaway effect for the "Level 1" text
        # Increase the fade_colour variable by 255/20,
        # causing the background colour to change until it reaches 255 (white)

        opacity -= 255 / 40
        fade_colour += 255 / 40

        # If the fade_colour variable's value is greater than 255 (white),
        # set it to black and change the screen to the first level
        # When the screen becomes black,
        # it means the fadeaway effect is done,

        if fade_colour > 255:
            opacity = 255
            fade_colour = 0
            screen = "level1"

    # Checks if the screen variable is equal to level1,
    # If it is, do the following things
    if screen == "level1":

        time = millis()
        # Creates the moving background (scrolling background)
        x_level1_background = constrain(x_level1_background, 0,
                                        background1.width - width)
        y_level1_background = constrain(y_level1_background, 0,
                                        background1.height - height)
        set(-x_level1_background, 0, background1)
        x_level1_background = frames
        powerup_scorepic.resize(powerup_size, powerup_size)
        powerup_heartpic.resize(powerup_size, powerup_size)
        giantLaserpic.resize(850, 150)

        # Score and lives text on the bottom of the screen
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)
        text("Score: " + str(score), width - 770, height - 30)

        # Creates the player
        fill(255, 255, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        # Checks if the up or down arrow keys are pressed
        # and moves the player in the corresponding directon
        if key_up is True:
            pos.y -= y_speed

        if key_down is True:
            pos.y += y_speed

        # Creates the lasers
        # Loops through the laser_list and
        # draws the lasers according to their location
        # They also have their own speed variable
        if key_space is True:
            if time >= last_shot + 350:
                laser_list.append(PVector(pos.x + player_size / 2, pos.y))
                last_shot = time

        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed

            # If the lasers reach the end of the screen,
            # remove the laser location from the list
            if lasers.x > width + 13:
                laser_list.remove(lasers)

        # If the enemy_spawn variable is set to false,
        # create enemies and add their randomized spawn
        # location to the list of enemies
        if enemy_spawn is False:
            enemy_list.append(PVector(random(width + enemy_size/2,
                                      width + enemy_size*5),
                                      random(0 + enemy_size/2,
                                      height - enemy_size/2)))

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
            fill(255)
            ellipse(enemy.x, enemy.y, enemy_size, enemy_size)
            enemy.x -= enemy_speed.x

            # If the enemies go past the left side of the screen,
            # remove them from the enemy list
            if enemy.x < 0 - enemy_size:
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
                centre_laser = PVector(lasers.x + 13, lasers.y + 5)
                dif = PVector.sub(centre_laser, enemy)

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

        # Random laser occurence to help player
        # If true do the following things
        if randomLaserOccurence:
            if frames == floor(giantLasertrigger):
                passedLasertrigger = time
                warningsign = True

        # Flashing warning on screen when
        # random laser occurence happens
        if warningsign:
            textAlign(CENTER, CENTER)
            textSize(108)
            fill(warningcolour)
            text("INCOMING!", width/2 + 20, height/2)
            if frames % 60 == 0:
                if warningcolour == 255:
                    warningcolour = 0
                else:
                    warningcolour = 255

        # If it's been 4 seconds since the giant laser
        # was triggered, create the laser
        if (time >= passedLasertrigger + 4000 and
           frames > floor(giantLasertrigger) and
           randomLaserOccurence):
            passedLasertrigger = 0
            warningsign = False

            pushMatrix()
            imageMode(CENTER)
            translate(width/2, 0)
            rotate(radians(90))
            image(giantLaserpic, giantLaser_loc, 0)

            # Makes the giant laser stay on screen for 3 seconds
            # after reaching the bottom of the screen
            if giantLaser_loc >= 0 + giantLaserpic.width/2 - 200:
                giantLaser_yspeed = 0
                if done_moving == 0:
                    done_moving = time
                giantLaserstopmove = True
                if time >= done_moving + 3000:
                    giantLaserstopmove = False
                    giantLaser_loc = 0 - giantLaserpic.width/2 - 200
                    randomLaserOccurence = False

            # giantLaser movement
            giantLaser_loc += giantLaser_yspeed
            popMatrix()

            # Collision detection between the giant laser
            # and the enemies, if they
            # hit the laser, they are removed
            if giantLaserstopmove:
                for enemy in enemy_list:
                    if enemy.x <= width/2 + 75 and enemy.x >= width/2 - 75:
                        enemy_list.remove(enemy)
                        break

        # Powerups
        # Once the frames has passed the trigger
        # For the associated powerup
        # start spawning that powerup

        fill(255, 0, 0)
        if frames >= powerup_heart_trigger:
            image(powerup_heartpic, powerup_heart_loc.x, powerup_heart_loc.y)
            powerup_heart_spawn = True

        if powerup_heart_spawn is True:
            powerup_heart_loc.sub(powerup_speed)

        if powerup_heart_loc.x < 0:
            powerup_heart_reset()

        # Finds the distance between the player and the heart powerup
        # If the player reaches the powerup
        # increase the player's hp by 1 if it's less than 5
        # Otherwise if hp is full, increase the score by 200
        # Then resets the powerup
        powerup_heart_centre = PVector(powerup_heart_loc.x + powerup_size/2,
                                       powerup_heart_loc.y + powerup_size/2)
        powerup_heart_dif = PVector.sub(pos, powerup_heart_centre)
        if powerup_heart_dif.mag() < player_size/2 + powerup_size/2:
            if lives == 5:
                score += 200
            else:
                lives += 1
            powerup_heart_reset()

        fill(0, 0, 255)
        if frames >= powerup_scoremultiply_trigger:
            image(powerup_scorepic, powerup_scoremultiply_loc.x,
                  powerup_scoremultiply_loc.y)
            powerup_scoremultiply_spawn = True

        if powerup_scoremultiply_spawn is True:
            powerup_scoremultiply_loc.sub(powerup_speed)

        if powerup_scoremultiply_loc.x < 0:
            powerup_scoremultiply_reset()

        # Finds the distance between the player
        # and the scoremultipler powerup
        # If the player reaches the powerup resets the powerup
        # Any enemy defeated now gives double the score
        # for a set duration of 20 seconds
        # After that returns to normal
        powerup_score_centre = PVector(powerup_scoremultiply_loc.x +
                                       powerup_size/2,
                                       powerup_scoremultiply_loc.y +
                                       powerup_size/2)
        powerup_score_dif = PVector.sub(pos, powerup_scoremultiply_loc)
        if powerup_score_dif.mag() < player_size/2 + powerup_size/2:
            countdown = True
            powerup_scoremultiply_reset()

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
            ellipse(boss_loc.x, boss_loc.y, boss_size, boss_size)

            if boss_hp > 0:

                fill(255)
                textSize(24)
                text("Boss HP: " + str(boss_hp), boss_loc.x - boss_size/2 - 13,
                     boss_loc.y + boss_size/2 + 25)

            # Boss Speed
            boss_loc.x -= boss_speed.x
            boss_attack.x -= boss_speed.x
            if boss_loc.x <= width - 100:
                boss_speed.x = 0

            # If the boss has not attacked
            # and is at a certain spot,
            # start attacking in the direction of the player
            if attacked is False and boss_loc.x <= width - 100:
                boss_dif = PVector.sub(boss_attack, pos)
                push = PVector.fromAngle(boss_dif.heading())
                push.mult(random(4, 6))
                boss_attackspeed = PVector(0, 0)
                boss_attackspeed.add(push)
                attacked = True

            # Boss' attack movement
            # Checks if the boss' attack hit the player
            # by finding the distance
            noStroke()
            ellipse(boss_attack.x, boss_attack.y, 20, 20)
            boss_attack.sub(boss_attackspeed)
            boss_hitplayer = PVector.sub(boss_attack, pos)
            stroke(0)

            # If hit player, reduce lives by 1 and add 1 to lives lost
            if boss_hitplayer.mag() < player_size/2:
                lives -= 1
                lives_lost += 1
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # If the boss' attack goes off the screen
            # Reset the boss' attack
            if boss_attack.x < 0:
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # Collision detection between
            # laser and boss
            # If a laser hits the boss
            # reduce its hp by 5
            for lasers in laser_list:
                centre_bosslaser = PVector(lasers.x + 13, lasers.y + 5)
                boss_dif = PVector.sub(centre_bosslaser, boss_loc)
                if boss_dif.mag() < boss_size/2:
                    laser_list.remove(lasers)
                    if boss_loc.x <= width - 100:
                        boss_hp -= laser_damage
                    break

            # If the boss' hp is 0
            # Call the bossdead function and do the actions within
            if boss_hp == 0:
                bossDead()

            # If the boss' hp is -1
            # After the bossdead function
            # Make it go off the screen
            # Then change the screen to the second level loading screen
            if boss_hp == -1:
                boss_loc.y += 2
                laser_damage = 0
                if boss_loc.y >= height + boss_size/2:
                    screen = "level_2_loadingscreen"

        frames += 1

        # Player boundaries
        if lives == 0:
            screen = "gameover1"

        if screen == 'gameover1':
            gameover()

        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

# -----------------------------------------------------------------
# -----------------------------------------------------------------

    if screen == "level_2_loadingscreen":

        # Fading background
        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 2", width / 2, height / 2)

        opacity -= 255 / 40
        fade_colour += 255 / 40
        if fade_colour > 255:
            fade_colour = 0
            opacity = 255
            reset_level()
            screen = "level2"

    if screen == "level2":
        time = millis()

        # Creates the scrolling background
        x_level2_background = constrain(x_level2_background, 0,
                                        background2.width - width)
        y_level2_background = constrain(y_level2_background, 0,
                                        background2.height - height)
        set(-x_level2_background, 0, background2)
        x_level2_background = frames
        powerup_scorepic.resize(powerup_size, powerup_size)
        powerup_heartpic.resize(powerup_size, powerup_size)
        giantLaserpic.resize(850, 150)

        # Creates the score and lives counter
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)
        text("Score: " + str(score), width - 770, height - 30)

        # Creates the player
        fill(255, 255, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        # Checks if the up or down arrow keys are pressed
        # and moves the player in the corresponding directon
        if key_up is True:
            pos.y -= y_speed

        if key_down is True:
            pos.y += y_speed

        # Creates the lasers
        # Loops through the laser_list and
        # draws the lasers according to their location
        # They also have their own speed variable
        if key_space is True:
            if time >= last_shot + 350:
                laser_list.append(PVector(pos.x + player_size / 2, pos.y))
                last_shot = time

        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed

            # If the lasers reach the end of the screen,
            # removes the laser location from the list
            if lasers.x > width + 13:
                laser_list.remove(lasers)

        # If the enemy_spawn variable is set to false,
        # create enemies and add their randomized
        # spawn location to the list of enemies
        if enemy_spawn is False:
            enemy_list.append(PVector(random(width + enemy_size/2,
                                      width + enemy_size*5),
                                      random(0 + enemy_size/2,
                                      height - enemy_size/2)))

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
            fill(255)
            ellipse(enemy.x, enemy.y, enemy_size, enemy_size)
            enemy.x -= enemy_speed.x * 1.5

            # If the enemies go past the left side of the screen,
            # remove them from the enemy list
            if enemy.x < 0 - enemy_size:
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
                centre_laser = PVector(lasers.x + 13, lasers.y + 5)
                dif = PVector.sub(centre_laser, enemy)

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

        # Random laser occurence to help player
        # If true do the following things
        if randomLaserOccurence:
            if frames == floor(giantLasertrigger):
                passedLasertrigger = time
                warningsign = True

        # Flashing warning on screen when
        # random laser occurence happens
        if warningsign:
            textAlign(CENTER, CENTER)
            textSize(108)
            fill(warningcolour)
            text("INCOMING!", width/2 + 20, height/2)
            if frames % 60 == 0:
                if warningcolour == 255:
                    warningcolour = 0
                else:
                    warningcolour = 255

        # If it's been 4 seconds since the giant laser
        # was triggered, create the laser
        if (time >= passedLasertrigger + 4000 and
           frames > floor(giantLasertrigger) and
           randomLaserOccurence):
            passedLasertrigger = 0
            warningsign = False

            pushMatrix()
            imageMode(CENTER)
            translate(width/2, 0)
            rotate(radians(90))
            image(giantLaserpic, giantLaser_loc, 0)

            # Makes the giant laser stay on screen for 3 seconds
            # after reaching the bottom of the screen
            if giantLaser_loc >= 0 + giantLaserpic.width/2 - 200:
                giantLaser_yspeed = 0
                if done_moving == 0:
                    done_moving = time
                giantLaserstopmove = True
                if time >= done_moving + 3000:
                    giantLaserstopmove = False
                    giantLaser_loc = 0 - giantLaserpic.width/2 - 200
                    randomLaserOccurence = False

            # giantLaser movement
            giantLaser_loc += giantLaser_yspeed
            popMatrix()

            # Collision detection between the giant laser
            # and the enemies, if they
            # hit the laser, they are removed
            if giantLaserstopmove:
                for enemy in enemy_list:
                    if enemy.x <= width/2 + 75 and enemy.x >= width/2 - 75:
                        enemy_list.remove(enemy)
                        break

        # Powerups
        # Once the frames has passed the trigger
        # For the associated powerup
        # start spawning that powerup

        fill(255, 0, 0)
        if frames >= powerup_heart_trigger:
            image(powerup_heartpic, powerup_heart_loc.x, powerup_heart_loc.y)
            powerup_heart_spawn = True

        if powerup_heart_spawn is True:
            powerup_heart_loc.sub(powerup_speed)

        if powerup_heart_loc.x < 0:
            powerup_heart_reset()

        # Finds the distance between the player and the heart powerup
        # If the player reaches the powerup
        # increase the player's hp by 1 if it's less than 5
        # Otherwise if hp is full, increase the score by 200
        # Then resets the powerup
        powerup_heart_centre = PVector(powerup_heart_loc.x + powerup_size/2,
                                       powerup_heart_loc.y + powerup_size/2)
        powerup_heart_dif = PVector.sub(pos, powerup_heart_centre)
        if powerup_heart_dif.mag() < player_size/2 + powerup_size/2:
            if lives == 5:
                score += 200
            else:
                lives += 1
            powerup_heart_reset()

        fill(0, 0, 255)
        if frames >= powerup_scoremultiply_trigger:
            image(powerup_scorepic, powerup_scoremultiply_loc.x,
                  powerup_scoremultiply_loc.y)
            powerup_scoremultiply_spawn = True

        if powerup_scoremultiply_spawn is True:
            powerup_scoremultiply_loc.sub(powerup_speed)

        if powerup_scoremultiply_loc.x < 0:
            powerup_scoremultiply_reset()

        # Finds the distance between the player
        # and the scoremultipler powerup
        # If the player reaches the powerup resets the powerup
        # Any enemy defeated now gives double the score
        # for a set duration of 20 seconds
        # After that returns to normal
        powerup_score_centre = PVector(powerup_scoremultiply_loc.x +
                                       powerup_size/2,
                                       powerup_scoremultiply_loc.y +
                                       powerup_size/2)
        powerup_score_dif = PVector.sub(pos, powerup_scoremultiply_loc)
        if powerup_score_dif.mag() < player_size/2 + powerup_size/2:
            countdown = True
            powerup_scoremultiply_reset()

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
            ellipse(boss_loc.x, boss_loc.y, boss_size, boss_size)

            if boss_hp > 0:

                fill(255)
                textSize(24)
                text("Boss HP: " + str(boss_hp), boss_loc.x - boss_size/2 - 13,
                     boss_loc.y + boss_size/2 + 25)

            # Boss Speed
            boss_loc.x -= boss_speed.x
            boss_attack.x -= boss.speed.x
            if boss_loc.x <= width - 100:
                boss_speed.x = 0

            # If the boss has not attacked
            # and is at a certain spot,
            # start attacking in the direction of the player
            if attacked is False and boss_loc.x <= width - 100:
                boss_dif = PVector.sub(boss_attack, pos)
                push = PVector.fromAngle(boss_dif.heading())
                push.mult(random(10, 12))
                boss_attackspeed = PVector(0, 0)
                boss_attackspeed.add(push)
                attacked = True

            # Boss' attack movement
            # Checks if the boss' attack hit the player
            # by finding the distance
            noStroke()
            ellipse(boss_attack.x, boss_attack.y, 20, 20)
            boss_attack.sub(boss_attackspeed)
            boss_hitplayer = PVector.sub(boss_attack, pos)
            stroke(0)

            # If hit player, reduce lives by 1 and add 1 to lives lost
            if boss_hitplayer.mag() < player_size/2:
                lives -= 1
                lives_lost += 1
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # If the boss' attack goes off the screen
            # Reset the boss' attack
            if boss_attack.x < 0:
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # Collision detection between
            # laser and boss
            # If a laser hits the boss
            # reduce its hp by 5
            for lasers in laser_list:
                centre_bosslaser = PVector(lasers.x + 13, lasers.y + 5)
                boss_dif = PVector.sub(centre_bosslaser, boss_loc)
                if boss_dif.mag() < boss_size/2:
                    laser_list.remove(lasers)
                    if boss_loc.x <= width - 100:
                        boss_hp -= laser_damage
                    break

            # If the boss' hp is 0
            # Call the bossdead function and do the actions within
            if boss_hp == 0:
                bossDead()

            # If the boss' hp is -1
            # After the bossdead function
            # Make it go off the screen
            # Change the screen to the third level loading screen
            if boss_hp == -1:
                boss_loc.y += 2
                laser_damage = 0
                if boss_loc.y >= height + boss_size/2:
                    screen = "level_3_loadingscreen"

        # Player boundaries
        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

        # If the player's lives reaches 0
        # Go to the gameover screen
        if lives == 0:
            screen = 'gameover2'

        if screen == 'gameover2':
            gameover()

        frames += 1

# ---------------------------------------------------
# ---------------------------------------------------

    if screen == "level_3_loadingscreen":

        # Fading background
        background(fade_colour, opacity)
        fill(255, 0, 0, opacity)
        textSize(58)
        textAlign(CENTER)
        text("LEVEL 3", width / 2, height / 2)
        opacity -= 255 / 40
        fade_colour += 255 / 40
        if fade_colour > 255:
            fade_colour = 0
            opacity = 255
            reset_level()
            screen = "level3"

    if screen == 'level3':

        # If the screen is level 3
        # Do the associated actions

        # Creates the moving background
        time = millis()
        x_level3_background = constrain(x_level3_background, 0,
                                        background2.width - width)
        y_level3_background = constrain(y_level3_background, 0,
                                        background2.height - height)
        set(-x_level3_background, 0, background3)
        x_level3_background = frames
        powerup_scorepic.resize(powerup_size, powerup_size)
        powerup_heartpic.resize(powerup_size, powerup_size)
        giantLaserpic.resize(850, 150)

        # Score and lives text on the bottom of the screen
        fill(255)
        textSize(30)
        textAlign(BOTTOM, RIGHT)
        text("Lives: " + str(lives), width - 130, height - 30)
        text("Score: " + str(score), width - 770, height - 30)

        # Creates the player
        fill(255, 255, 0)
        ellipse(pos.x, pos.y, player_size, player_size)

        # Checks if the up or down arrow keys are pressed and
        # moves the player in the corresponding directon
        if key_up is True:
            pos.y -= y_speed

        if key_down is True:
            pos.y += y_speed

        # Creates the lasers
        # Loops through the laser list and draws
        # the laser according to their location
        # They also have their own speed variable
        if key_space is True:
            if time >= last_shot + 350:
                laser_list.append(PVector(pos.x + player_size / 2, pos.y))
                last_shot = time

        for lasers in laser_list:
            fill(0, 255, 0)
            rect(lasers.x, lasers.y, 26, 10)
            lasers.x += laser_speed

            # If the lasers reach the end of the screen,
            # removes the laser location from the list
            if lasers.x > width + 13:
                laser_list.remove(lasers)

        # If the enemy_spawn variable is set to false, create enemies and
        # add their randomized spawn location to the list of enemies
        if enemy_spawn is False:
            enemy_list.append(PVector(random(width + enemy_size/2,
                                      width + enemy_size*5),
                                      random(0 + enemy_size/2,
                                      height - enemy_size/2)))

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
            fill(255)
            ellipse(enemy.x, enemy.y, enemy_size, enemy_size)
            enemy.x -= enemy_speed.x * 2

            # If the enemies go past the left side of the screen,
            # remove them from the enemy list
            if enemy.x < 0 - enemy_size:
                enemy_list.remove(enemy)

            # Collision Detection
            # If an enemy hits the player,
            # the number of lives will decrease by 1
            # and the number of lives lost will increase by 1
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
                centre_laser = PVector(lasers.x + 13, lasers.y + 5)
                dif = PVector.sub(centre_laser, enemy)

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

        # Random laser occurence to help player
        # If true do the following things
        if randomLaserOccurence:
            if frames == floor(giantLasertrigger):
                passedLasertrigger = time
                warningsign = True

        # Flashing warning on screen when
        # random laser occurence happens
        if warningsign:
            textAlign(CENTER, CENTER)
            textSize(108)
            fill(warningcolour)
            text("INCOMING!", width/2 + 20, height/2)
            if frames % 60 == 0:
                if warningcolour == 255:
                    warningcolour = 0
                else:
                    warningcolour = 255

        # If it's been 4 seconds since the giant laser
        # was triggered, create the laser
        if (time >= passedLasertrigger + 4000 and
           frames > floor(giantLasertrigger) and
           randomLaserOccurence):
            passedLasertrigger = 0
            warningsign = False

            pushMatrix()
            imageMode(CENTER)
            translate(width/2, 0)
            rotate(radians(90))
            image(giantLaserpic, giantLaser_loc, 0)

            # Makes the giant laser stay on screen for 3 seconds
            # after reaching the bottom of the screen
            if giantLaser_loc >= 0 + giantLaserpic.width/2 - 200:
                giantLaser_yspeed = 0
                if done_moving == 0:
                    done_moving = time
                giantLaserstopmove = True
                if time >= done_moving + 3000:
                    giantLaserstopmove = False
                    giantLaser_loc = 0 - giantLaserpic.width/2 - 200
                    randomLaserOccurence = False

            # giantLaser movement
            giantLaser_loc += giantLaser_yspeed
            popMatrix()

            # Collision detection between the giant laser
            # and the enemies, if they
            # hit the laser, they are removed
            if giantLaserstopmove:
                for enemy in enemy_list:
                    if enemy.x <= width/2 + 75 and enemy.x >= width/2 - 75:
                        enemy_list.remove(enemy)
                        break

        # Powerups
        # Once the frames has passed the trigger
        # For the associated powerup
        # start spawning that powerup

        fill(255, 0, 0)
        if frames >= powerup_heart_trigger:
            image(powerup_heartpic, powerup_heart_loc.x, powerup_heart_loc.y)
            powerup_heart_spawn = True

        if powerup_heart_spawn is True:
            powerup_heart_loc.sub(powerup_speed)

        if powerup_heart_loc.x < 0:
            powerup_heart_reset()

        # Finds the distance between the player and the heart powerup
        # If the player reaches the powerup
        # increase the player's hp by 1 if it's less than 5
        # Otherwise if hp is full, increase the score by 200
        # Then resets the powerup
        powerup_heart_centre = PVector(powerup_heart_loc.x + powerup_size/2,
                                       powerup_heart_loc.y + powerup_size/2)
        powerup_heart_dif = PVector.sub(pos, powerup_heart_centre)
        if powerup_heart_dif.mag() < player_size/2 + powerup_size/2:
            if lives == 5:
                score += 200
            else:
                lives += 1
            powerup_heart_reset()

        fill(0, 0, 255)
        if frames >= powerup_scoremultiply_trigger:
            image(powerup_scorepic, powerup_scoremultiply_loc.x,
                  powerup_scoremultiply_loc.y)
            powerup_scoremultiply_spawn = True

        if powerup_scoremultiply_spawn is True:
            powerup_scoremultiply_loc.sub(powerup_speed)

        if powerup_scoremultiply_loc.x < 0:
            powerup_scoremultiply_reset()

        # Finds the distance between the player
        # and the scoremultipler powerup
        # If the player reaches the powerup resets the powerup
        # Any enemy defeated now gives double the score
        # for a set duration of 20 seconds
        # After that returns to normal
        powerup_score_centre = PVector(powerup_scoremultiply_loc.x +
                                       powerup_size/2,
                                       powerup_scoremultiply_loc.y +
                                       powerup_size/2)
        powerup_score_dif = PVector.sub(pos, powerup_scoremultiply_loc)
        if powerup_score_dif.mag() < player_size/2 + powerup_size/2:
            countdown = True
            powerup_scoremultiply_reset()

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
            ellipse(boss_loc.x, boss_loc.y, boss_size, boss_size)

            if boss_hp > 0:

                fill(255)
                textSize(24)
                text("Boss HP: " + str(boss_hp), boss_loc.x - boss_size/2 - 13,
                     boss_loc.y + boss_size/2 + 25)

            # Boss Speed
            boss_loc.x -= boss_speed.x
            boss_attack.x -= boss_speed.x
            if boss_loc.x <= width - 100:
                boss_speed.x = 0

            # If the boss has not attacked
            # and is at a certain spot,
            # start attacking in the direction of the player
            if attacked is False and boss_loc.x <= width - 100:
                boss_dif = PVector.sub(boss_attack, pos)
                push = PVector.fromAngle(boss_dif.heading())
                push.mult(random(14, 18))
                boss_attackspeed = PVector(0, 0)
                boss_attackspeed.add(push)
                attacked = True

            # Boss' attack movement
            # Checks if the boss' attack hit the player
            # by finding the distance
            noStroke()
            ellipse(boss_attack.x, boss_attack.y, 20, 20)
            boss_attack.sub(boss_attackspeed)
            boss_hitplayer = PVector.sub(boss_attack, pos)
            stroke(0)

            # If hit player, reduce lives by 1 and add 1 to lives lost
            if boss_hitplayer.mag() < player_size/2:
                lives -= 1
                lives_lost += 1
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # If the boss' attack goes off the screen
            # Reset the boss' attack
            if boss_attack.x < 0:
                boss_attack.x = boss_loc.x
                boss_attack.y = height/2
                attacked = False

            # Collision detection between
            # laser and boss
            # If a laser hits the boss
            # reduce its hp by 5
            for lasers in laser_list:
                centre_bosslaser = PVector(lasers.x + 13, lasers.y + 5)
                boss_dif = PVector.sub(centre_bosslaser, boss_loc)
                if boss_dif.mag() < boss_size/2:
                    laser_list.remove(lasers)
                    if boss_loc.x <= width - 100:
                        boss_hp -= laser_damage
                    break

            # If the boss' hp is 0
            # Call the bossdead function and do the actions within
            if boss_hp == 0:
                bossDead()

            # If the boss' hp is -1
            # After the bossdead function
            # Make the boss' size decrease
            # Until it becomes 0
            # Then go to the ending screen
            if boss_hp == -1:
                laser_damage = 0
                boss_size -= 1
                if boss_size <= 0:
                    frames = 0
                    screen = 'ending'

        frames += 1

        if lives == 0:
            screen = "gameover1"

        if screen == 'gameover1':
            gameover()

        if pos.y - player_size / 2 <= 0:
            pos.y = 0 + player_size / 2

        if pos.y + player_size / 2 >= height:
            pos.y = height - player_size / 2

    if screen == 'ending':

        # If the screen is the ending screen do these things
        # Congratulatory message
        if frames < 300:
            background(0)
            textAlign(CENTER)
            textSize(48)
            fill(colour1, colour2, colour3)
            powerup_scorepic.resize(powerup_size, powerup_size)

            pushMatrix()
            translate(125, 280)
            imageMode(CENTER)
            rotate(radians(angle))
            image(powerup_scorepic, 0, 0)
            popMatrix()

            pushMatrix()
            translate(675, 280)
            imageMode(CENTER)
            rotate(radians(angle))
            image(powerup_scorepic, 0, 0)
            popMatrix()

            if frames % 10 == 0:
                colour1 = random(255)
                colour2 = random(255)
                colour3 = random(255)
            text("CONGRATULATIONS!!", width/2, height/2)

        else:
            # Shows the total score and lives lost
            # Adds the corresponding bonus to
            # total score based on the number of
            # lives lost
            # Then give a grade based on the final score
            if frames < 600:
                background(0)
                textAlign(CENTER, CENTER)
                textSize(40)
                fill(255)
                text("Total Score: " + str(total_score),
                     width/2, height/2 - 100)
                text("Lives Lost: " + str(lives_lost), width/2, height/2)
            elif frames < 800 and frames > 600:
                if lives_lost <= 3:
                    bonus = 1000
                elif lives_lost <= 5:
                    bonus = 500
                elif lives_lost <= 8:
                    bonus = 100
                else:
                    bonus = 0
                fill(255)
                background(0)
                text("Total Score: " + str(total_score) + " + " + str(bonus),
                     width / 2, height / 2 - 100)
            elif frames > 800:
                background(0)
                if total_score >= 12000:
                    grade = 'S'
                elif total_score >= 8000:
                    grade = 'A'
                elif total_score >= 5000:
                    grade = 'B'
                elif total_score >= 3000:
                    grade = 'C'
                elif total_score >= 1000:
                    grade = 'D'
                else:
                    grade = 'F'
                # Options to go the menu or exit
                # Change colours when hovered over
                fill(255)
                textSize(40)
                text("Total Score: " + str(total_score + bonus),
                     width/2, height/2 - 100)
                text("Grade: " + grade, width/2, height/2 + 100)

                fill(hover_colour1[0], hover_colour1[1], hover_colour1[2])
                rect(width - 760, height - 70, 100, 60)
                fill(hover_colour2[0], hover_colour2[1], hover_colour2[2])
                rect(width - 140, height - 70, 100, 60)

                fill(0)
                textSize(28)
                text("Quit", width - 710, height - 45)
                text("Menu", width - 90, height - 45)
                center_quit_square = PVector(width - 760 + 50,
                                             height - 70 + 30)
                center_replay_square = PVector(width - 140 + 50,
                                               height - 70 + 30)
                diff_quit_sq = PVector(mouseX - center_quit_square.x,
                                       mouseY - center_quit_square.y)
                diff_replay_sq = PVector(mouseX - center_replay_square.x,
                                         mouseY - center_replay_square.y)

                if (diff_quit_sq.x >= -50 and diff_quit_sq.x <= 50 and
                   diff_quit_sq.y >= -30 and diff_quit_sq.y <= 30):
                    hover_colour1[0] = 0
                    hover_colour1[1] = 206
                    hover_colour1[2] = 209
                    if click is True:
                        exit()

                if (diff_quit_sq.x <= -50 or diff_quit_sq.x >= 50 or
                   diff_quit_sq.y <= -30 or diff_quit_sq.y >= 30):
                    hover_colour1[0] = 175
                    hover_colour1[1] = 238
                    hover_colour1[2] = 238

                if (diff_replay_sq.x >= -50 and diff_replay_sq.x <= 50 and
                   diff_replay_sq.y >= -30 and diff_replay_sq.y <= 30):
                    hover_colour2[0] = 0
                    hover_colour2[1] = 206
                    hover_colour2[2] = 209
                    if click is True:
                        reset_level()
                        screen = 'menu'

                if (diff_replay_sq.x <= -50 or diff_replay_sq.x >= 50 or
                   diff_replay_sq.y <= -30 or diff_replay_sq.y >= 30):
                    hover_colour2[0] = 175
                    hover_colour2[1] = 238
                    hover_colour2[2] = 238

        frames += 1
        angle += 3


def mousePressed():
    # Actions to do when a mouse button is pressed
    global click
    if mouseButton == LEFT:
        click = True


def mouseReleased():
    # Actions to do when the mouse button is released
    global click
    if mouseButton == LEFT:
        click = False


def keyPressed():
    # Actions to do when a specific key is pressed
    # Used for the movement and shooting of the player
    global key_up
    global key_down
    global key_space
    global laser_list
    global last_shot
    global screen

    if key == CODED:
        if keyCode == UP:
            key_up = True
        elif keyCode == DOWN:
            key_down = True

    if key == " ":
        key_space = True
        if "gameover" in screen:
            reset_level()


def keyReleased():
    # Actions to do when the specific keys are released
    # Prevents weird movement of player
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
