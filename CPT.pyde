y_speed = 10
laser_speed = 10
player_size = 50
pos = PVector(0 + player_size/2,300)
laser_loc = PVector(pos.x + player_size/2,pos.y)
keys1 = False
keys2 = False
keys3 = False

def setup():
    size(800,600)

def draw():
    global speed
    global pos
    global keys1
    global keys2 
    global keys3
    global laser_speed
    global laser_loc
    background(255)
    fill(255,0,0)
    ellipse(pos.x,pos.y,player_size,player_size)
    
    if keys1 == True:
        pos.y -= y_speed
    if keys2 == True:
        pos.y += y_speed
        
    if keys3 == True:
        rect(laser_loc.x,laser_loc.y,25,10)
        laser_loc.x += laser_speed
        
    if pos.y - player_size/2 <= 0:
        pos.y = 0 + player_size/2
        
    if pos.y + player_size/2 >= height:
        pos.y = height - player_size/2
    
    if laser_loc.x >= width:
        laser_loc.x = pos.x + player_size/2
        keys3 = False
        

    
def keyPressed():
    global keys1
    global keys2
    global keys3
    global laser_loc
    if key == CODED:
        if keyCode == UP:
            keys1 = True
            
    if key == CODED:
        if keyCode == DOWN:
            keys2 = True
    
    if key == ' ':
        keys3 = True
        laser_loc.y = pos.y    
            
def keyReleased():
    global keys1
    global keys2 
    global keys3
    if key == CODED:
        if keyCode == UP:
            keys1 = False

    if key == CODED:
        if keyCode == DOWN:
            keys2 = False
            
    
    
