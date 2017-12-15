play = False
menu = False
instructions = False
y_speed = 10
laser_speed = 10
player_size = 50
pos = PVector(0 + player_size/2,300)
laser_loc = PVector(pos.x + player_size/2,pos.y)
laser_list = []
key_up =  False
key_down = False
key_space = False
click = False
hover_colour1 = [175,238,238]
hover_colour2 = [175,238,238]
hover_colour3 = [175,238,238]
hover_colour4 = [175,238,238]

def setup():
    size(800,600)
    
def draw():
    global speed
    global pos
    global key_up
    global key_down
    global key_space
    global laser_speed
    global laser_loc
    global hover_colour1
    global hover_colour2
    global hover_colour3
    global hover_colour4
    global click
    global play
    global menu
    global instructions
    
    if menu == False:
        
        background(255)
        textSize(48)
        strokeWeight(4)
        textAlign(CENTER,CENTER)
        fill(0)
        text("Airplane Shooting Game", width/2, height/2 - 50)
            
        fill(hover_colour1[0],hover_colour1[1],hover_colour1[2])
        rect(width - 110, height - 260,68,58)
        fill(hover_colour2[0],hover_colour2[1],hover_colour2[2])
        rect(width - 230, height - 190, 188, 58)
        fill(hover_colour3[0],hover_colour3[1],hover_colour3[2])
        rect(width - 112, height - 120, 68, 58)
            
        textSize(28)
        strokeWeight(2)
        textAlign(RIGHT, RIGHT)
        fill(0)
        text("Play",width - 50, height - 220)
        text("How To Play", width - 50, height - 150)
        text("Quit",width - 50, height - 80)
            
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
                click = False
                play = True
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
        text("How To Play", width/2, height/2 - 250)
        textSize(24)
        textAlign(LEFT)
        text("Control your character with the arrow keys; UP and DOWN.", 65, 140)
        text("Use the Spacebar to shoot your weapon.", 65, 175)
        text("You have 3 lives, when you reach 0 lives, you lose.", 65, 210) 
        text("Each level resets your lives to 3.", 65, 245)
        text("Each level has many enemies. There are 3 levels in total.", 65, 280) 
        text("Each enemy defeated gives a bonus to your score.",65,315)
        text("Each level has a boss at the end. Defeating it clears the level.",65, 350)
        fill(hover_colour4[0], hover_colour4[1], hover_colour4[2])
        rect(width - 760, height - 80, 70,50)
        fill(0)
        text("Back",width - 750, height - 50)
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
                
        
        
        
def mousePressed():
    global click
    if mouseButton == LEFT:
        click = True
    
def mouseReleased():
    global click
    if mouseButton == LEFT:
        click = False
    

    
    if play == True:
        
        print(keyCode)
        background(255)
        fill(255,0,0)
        ellipse(pos.x,pos.y,player_size,player_size)
            
        if key_up == True:
            pos.y -= y_speed
            
        if key_down == True:
            pos.y += y_speed
            
        if pos.y - player_size/2 <= 0:
            pos.y = 0 + player_size/2
            
        if pos.y + player_size/2 >= height:
            pos.y = height - player_size/2
        
        if laser_loc.x >= width:
            laser_loc.x = pos.x + player_size/2
            laser_list.remove(laser_loc)


def keyPressed():
    global key_up
    global key_down
    global key_space
    global laser_loc
    if key == CODED:
        if keyCode == UP:
            key_up = True
            
    if key == CODED:
        if keyCode == DOWN:
            key_down = True
    
    if key == ' ':
        laser_list.append(laser_loc)
        key_space = True
            
            
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
    
    if key == ' ':
        key_space = False


    

            

            
    
    
