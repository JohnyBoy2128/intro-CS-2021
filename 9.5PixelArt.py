import simplegui

def draw_handler(canvas):
    colors = [] 
    colors.append (["#493332", "#493332", "#493332", "#A7A9B1", "#A7A9B1", "#A7A9B1","#A7A9B1","#493332"]) 
    colors.append (["#493332", "#493332", "#493332", "#A7A9B1", "#A7A9B1", "#A7A9B1","#493332","#493332"]) 
    colors.append (["#FFFFFF", "#FFFFFF", "#493332", "#A7A9B1", "#A7A9B1", "#493332","#FFFFFF","#FFFFFF"]) 
    colors.append (["#000000", "#FFFFFF", "#493332", "#A7A9B1", "#493332", "#493332","#FFFFFF","#000000"]) 
    colors.append (["#493332", "#493332", "#493332", "#493332", "#493332", "#493332","#493332","#493332"]) 
    colors.append (["#493332", "#493332", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF","#493332","#493332"]) 
    colors.append (["#493332", "#FFFFFF", "#000000", "#A7A9B1", "#A7A9B1", "#000000","#FFFFFF","#493332"]) 
    colors.append (["#493332", "#FFFFFF", "#A7A9B1", "#A7A9B1", "#A7A9B1", "#A7A9B1","#FFFFFF","#493332"]) 

    row = 0
    col = 0
    for r in range(1, 400, 50):
        for c in range(1, 400, 50):
            canvas.draw_polygon([(c, r), (c + 50, r), (c + 50, r + 50), (c, r + 50)], 1, "black", colors[row][col])   
            col = col + 1
        row = row + 1
        col = 0

#********** MAIN **********
frame = simplegui.create_frame('Pic', 400, 400)
frame.set_draw_handler(draw_handler)
frame.start()
