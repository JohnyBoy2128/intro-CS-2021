import simplegui

def draw_handler(canvas):

    # makes count a global variable, recognized outside this subprogram
    global count
    # adds one to the count each time the frame is redrawn
    count = count + 1
    # makes global a global variable, recognized outside this subprogram
    global colors

    # by resetting the count to 0 after the frame is redrawn 250 times, prevents program from crashing and by stopping at 250, we see the "raindrop" fall over and over again
    if (count > 150):                        
        count = 0

    # Gives the cross eyed thingy
    if (count == 30):
        colors[3][0] = "#FFFFFF"
        colors[2][1] = "#000000"
        colors[3][7] = "#FFFFFF"
        colors[2][6] = "#000000"

    # This makes the wonderful tounge
    if (count == 50):
        colors[7][3] = "Red"
        colors[7][4] = "Red"

    # Tears begin to fall from the left eye
    if (count == 70):
        # resetting end of loop
        colors [7][1] = "#FFFFFF"
        colors [7][6] = "#FFFFFF"
       
        # left eye 1st
        colors[4][1] = "#80e5ff"

    if (count == 90):
        # left eye 2nd
        colors [5][1] = "#80e5ff"
        # right eye 1st             
        colors [4][6] = "#80e5ff"
        # returns the box above left tear back to brown
        colors [4][1] = "#493332"

    # teardrop continues falling to the next position
    if (count == 110):
        # left eye 3rd
        colors [7][1] = "#80e5ff"
        # right eye 2nd
        colors [5][6] = "#80e5ff"
        # reseting block above left tear
        colors [5][1] = "#493332"
        # reseting block above right tear
        colors [4][6] = "#493332"

    # "raindrop" continues falling to the next position
    if (count == 130):
        # right eye 3rd
        colors [7][6] = "#80e5ff"
        # reseting block above left eye
        colors [5][1] = "#493332"
        # reseting block above right eye
        colors [5][6] = "#493332"



    # returns the square that is the final position of the "raindrop" to the blue sky color
    if (count == 330):
        colors [5][4] = "#80e5ff"

    # actually draws the array colors described by the code above
    row = 0
    col = 0
    for r in range(1, 400, 50):
        for c in range(1, 400, 50):
            canvas.draw_polygon([(c, r), (c + 50, r), (c + 50, r + 50), (c, r + 50)], 1, "black", colors[row][col])
            col = col + 1
        row = row + 1
        col = 0

#********** MAIN **********
# count inside the draw_handler subprogram will restart only once before reaching 250, instead of resetting each time 
# the frame is redrawn.
count = 1
frame = simplegui.create_frame('Pic', 400, 400)
frame.set_draw_handler(draw_handler)
frame.start()

# the variable colors has been moved to the main program so that the rain cloud will be permanent
colors = [] 
colors.append (["#493332", "#493332", "#493332", "#A7A9B1", "#A7A9B1", "#A7A9B1","#A7A9B1","#493332"]) 
colors.append (["#493332", "#493332", "#493332", "#A7A9B1", "#A7A9B1", "#A7A9B1","#493332","#493332"]) 
colors.append (["#FFFFFF", "#FFFFFF", "#493332", "#A7A9B1", "#A7A9B1", "#493332","#FFFFFF","#FFFFFF"]) 
colors.append (["#000000", "#FFFFFF", "#493332", "#A7A9B1", "#493332", "#493332","#FFFFFF","#000000"]) 
colors.append (["#493332", "#493332", "#493332", "#493332", "#493332", "#493332","#493332","#493332"]) 
colors.append (["#493332", "#493332", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF","#493332","#493332"]) 
colors.append (["#493332", "#FFFFFF", "#000000", "#A7A9B1", "#A7A9B1", "#000000","#FFFFFF","#493332"]) 
colors.append (["#493332", "#FFFFFF", "#A7A9B1", "#A7A9B1", "#A7A9B1", "#A7A9B1","#FFFFFF","#493332"]) 