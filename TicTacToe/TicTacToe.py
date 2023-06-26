import time
import thumby
import math
import random

face_bytearray = bytearray([223,157,57,127,127,57,157,223])
x_bytearray = bytearray([126,189,219,231,231,219,189,126])
o_bytearray = bytearray([255,195,189,189,189,189,195,255])

# BITMAP: width: 80, height: 80
# map_bytearray = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,1,128,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,130,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,68,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,225,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,87,42,36,118,34,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,243,249,249,243,243,241,231,227,235,231,251,239,243,235,231,251,251,231,251,235,243,255,233,15,0,235,255,251,225,255,235,243,243,239,251,235,251,235,251,251,239,251,255,235,251,255,250,235,250,251,250,255,242,64,234,49,9,240,240,252,250,255,252,252,254,248,252,254,252,252,248,252,252,254,252,254,252,252,252,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,39,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,191,234,255,253,0,187,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,40,0,224,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,106,255,255,81,104,255,221,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,255,255,255,255,127,127,127,127,127,127,255,127,255,127,127,255,127,255,127,255,127,255,255,96,0,127,255,255,127,127,255,255,255,255,127,255,255,255,255,127,255,255,255,191,255,127,255,191,255,191,255,63,37,191,19,20,255,63,170,255,255,191,255,191,255,191,191,191,255,191,191,191,255,255,255,255,255,255,255,
#           254,254,252,252,254,252,254,255,254,253,254,254,255,254,253,254,254,254,255,252,255,254,254,8,4,224,255,255,254,255,252,254,255,255,254,253,255,254,255,254,254,252,255,254,255,255,255,254,255,255,254,254,253,168,184,245,34,253,46,248,252,251,252,254,252,254,248,252,252,249,249,250,249,249,249,249,251,253,251,251,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,3,248,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,10,224,31,32,245,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,3,0,239,224,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])

# # BITMAP: width: 72, height: 40
# map_bytearray = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,71,39,237,51,100,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,64,144,235,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           127,127,127,127,255,255,127,255,127,255,255,255,255,255,255,255,255,255,255,255,255,124,244,204,237,239,255,255,255,255,255,127,255,255,255,255,127,255,255,255,255,127,255,255,127,127,127,127,63,127,127,63,127,127,58,109,89,63,127,127,63,127,63,255,63,127,63,127,63,127,63,63,
#           255,255,255,255,255,254,255,254,254,255,254,255,254,255,254,255,254,254,255,254,254,122,238,120,158,190,255,254,254,254,254,254,254,255,254,254,254,254,255,254,254,254,254,254,255,255,255,255,255,255,255,255,255,223,206,122,188,183,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
#           223,223,223,223,239,255,239,255,239,239,239,239,239,239,239,223,223,223,223,223,223,75,15,218,183,151,223,255,223,223,255,223,223,223,223,255,223,223,223,223,191,255,255,159,255,159,255,191,255,175,255,175,255,143,125,71,251,207,255,215,223,247,223,247,215,247,223,247,215,223,247,215,
#           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,5,13,244,241,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,189,93,102,215,239,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])
           
           
           # BITMAP: width: 72, height: 40
map_bytearray = bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,184,216,18,204,155,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,191,111,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           128,128,128,128,0,0,128,0,128,0,0,0,0,0,0,0,0,0,0,0,0,131,11,51,18,16,0,0,0,0,0,128,0,0,0,0,128,0,0,0,0,128,0,0,128,128,128,128,192,128,128,192,128,128,197,146,166,192,128,128,192,128,192,0,192,128,192,128,192,128,192,192,
           0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,1,133,17,135,97,65,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,32,49,133,67,72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           32,32,32,32,16,0,16,0,16,16,16,16,16,16,16,32,32,32,32,32,32,180,240,37,72,104,32,0,32,32,0,32,32,32,32,0,32,32,32,32,64,0,0,96,0,96,0,64,0,80,0,80,0,112,130,184,4,48,0,40,32,8,32,8,40,8,32,8,40,32,8,40,
           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,242,11,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,66,162,153,40,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           
          

# BITMAP: width: 72, height: 40
o_top_left_byte_array = bytearray([255,255,127,159,207,247,255,239,239,95,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,248,243,247,247,247,243,249,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])
           
           
# BITMAP: width: 2, height: 40
vertical_line_byte_array = bytearray([255,255,
           255,255,
           255,255,
           255,255,
           255,255])      
           
           
# BITMAP: width: 20, height: 20
o_test = bytearray([0,0,192,48,24,8,14,6,4,4,4,4,4,4,4,4,28,240,0,0,
           0,0,15,120,128,0,0,0,0,0,0,0,0,0,0,0,0,1,255,0,
           0,0,0,0,1,3,6,4,4,4,4,4,4,4,4,6,2,1,0,0])

# # BITMAP: width: 10, height: 10
# o_byte_array = bytearray([0,252,2,2,2,2,2,2,252,0,
#           0,0,1,1,1,1,1,1,0,0]
           
# BITMAP: width: 8, height: 8
o_byte_array_black = bytearray([0,126,66,66,66,66,126,0])

# BITMAP: width: 8, height: 8
o_byte_array_white = bytearray([255,129,189,189,189,189,129,255])


# BITMAP: width: 8, height: 8
x_byte_array = bytearray([193,99,54,28,12,52,35,193])
           
           
# BITMAP: width: 72, height: 2
horizontal_line_byte_array = bytearray([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
           
           

# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = thumby.Sprite(32, 32, face_bytearray)

left_vertical_line_sprite = thumby.Sprite(2, 40, vertical_line_byte_array, x=20, y=0)
right_vertical_line_sprite = thumby.Sprite(2, 40, vertical_line_byte_array, x=50, y=0)
top_horitontal_line_sprite = thumby.Sprite(72, 2, horizontal_line_byte_array, x=0, y=10)
bottom_horitontal_line_sprite = thumby.Sprite(72, 2, horizontal_line_byte_array, x=0, y=25)
o_top_left_sprite_white = thumby.Sprite(8, 8, o_byte_array_white, x=0, y=0)
o_top_left_sprite_black = thumby.Sprite(8, 8, o_byte_array_black, x=0, y=0)

mapSprite = thumby.Sprite(72, 40, map_bytearray)

# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)

blink = True

o_sprite = o_top_left_sprite_black

board = [['', '', ''],
        ['', '', ''],
        ['','','']]
        
        
board_sprites = [[(0, 0), (30, 0), (60, 0),], 
                [(0, 15), (30, 15), (60, 15)],
                [(0, 30), (30, 30), (60, 30)]]
        
targeting_square = [0, 0] #x, y

def get_elements_to_render():
    for y, row in enumerate(board):
        for x, square in enumerate(row):
            if square == 'X' and type(board_sprites[y][x]) == tuple:
                x_val,y_val = board_sprites[y][x]
                print("setting x at: ", x_val, y_val)
                board_sprites[y][x] = thumby.Sprite(8, 8, x_byte_array, x=x_val, y=y_val)
                print(board_sprites)
            elif square == 'O' and type(board_sprites[y][x]) == tuple:
                x_val,y_val = board_sprites[y][x]
                print("setting O at: ", x_val, y_val)
                board_sprites[y][x] = thumby.Sprite(8, 8, o_byte_array_white, x=x_val, y=y_val)
                print(board_sprites)
                
                
    for row in board_sprites:
        for s in row:
            if type(s) != tuple:
                yield s
                
    # return [b for row in board_sprites for b in row if type(b) != tuple]
 
while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0)
    
    if thumby.buttonD.justPressed():
        targeting_square[1] += 1
        o_top_left_sprite_white.y += 15
        o_top_left_sprite_black.y += 15
        
    
    if thumby.buttonU.justPressed():
        targeting_square[1] -= 1
        o_top_left_sprite_white.y -= 15
        o_top_left_sprite_black.y -= 15
        
        
    if thumby.buttonR.justPressed():
        targeting_square[0] += 1
        o_top_left_sprite_white.x += 30
        o_top_left_sprite_black.x += 30
        
        
    if thumby.buttonL.justPressed():
        targeting_square[0] -= 1
        o_top_left_sprite_white.x -= 30
        o_top_left_sprite_black.x -= 30
        
        
    if thumby.buttonA.justPressed():
        if board[targeting_square[1]][targeting_square[0]] == '':
            board[targeting_square[1]][targeting_square[0]] = 'O'
            
            ai_moving = True
            while ai_moving:
                random_sqare = board[random.randint(0,2)][random.randint(0,2)]
                if random_sqare == "":
                    board[random.randint(0,2)][random.randint(0,2)] = "X"
                    ai_moving = False
                    
            
    
    # print(targeting_square)
    # print(board)
        
    
    if t0 % 10 == 0:
        if blink: 
            o_sprite = o_top_left_sprite_white
            # print(blink)
        else:
            o_sprite = o_top_left_sprite_black
        blink = False if blink else True
        
        
    
        
    
        
            
    
    
    sprites_to_render = list(get_elements_to_render())
    # print(board_sprites)
    print("len sprites to render:", len(sprites_to_render))
    
    for sprite in sprites_to_render:
        thumby.display.drawSprite(sprite)
        
        
    thumby.display.drawSprite(o_sprite)
        
    
    thumby.display.drawSprite(left_vertical_line_sprite)
    thumby.display.drawSprite(right_vertical_line_sprite)
    thumby.display.drawSprite(top_horitontal_line_sprite)
    thumby.display.drawSprite(bottom_horitontal_line_sprite)
    thumby.display.update()
    
    
    
    
    
    
    
    
    
    
