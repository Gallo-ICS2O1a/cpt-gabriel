y_speed = 10
laser_speed = 10
player_size = 50
pos = PVector(0 + player_size/2,300)
laser_loc = PVector(pos.x + player_size/2,pos.y)
laser_list = []
key_up =  False
key_down = False
key_space = False

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
    background(255)
    fill(255,0,0)
    ellipse(pos.x,pos.y,player_size,player_size)
        
    if key_up == True:
        pos.y -= y_speed
        
    if key_down == True:
        pos.y += y_speed
        
    for lasers in laser_list:
        if len(laser_list) > 0:
            rect(laser_loc.x,laser_loc.y,25,10)
        laser_loc.x += laser_speed
        
        
            
        
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
            

            
    
    
