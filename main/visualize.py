from PIL import Image, ImageDraw

def draw(game):
    image = create_image(game)
    image.show()

def create_image(game):
    field_image = create_field_image()
    for pos in game.field.keys():
        if game.field[pos] != None:
            draw_figure(field_image, game.field[pos], pos)
    return field_image

def create_field_image():
    field =  Image.new('L', (96, 96), 255)
    
    draw = ImageDraw.Draw(field, 'L')
    draw.line((0,31, 96, 31), 0, 3)
    draw.line((0,63, 96, 63), 0, 3)
    draw.line((31,0, 31, 96), 0, 3)
    draw.line((63,0, 63, 96), 0, 3)
    
    return field

def draw_figure(field, fig, pos):
    d = ImageDraw.Draw(field)
    if fig == 'X':
        offset = 5
        d.line((pos[0]*32+offset, pos[1]*32+offset, pos[0]*32+32-offset, pos[1]*32+32-offset), 0, 3)
        d.line((pos[0]*32+32-offset, pos[1]*32+offset, pos[0]*32+offset, pos[1]*32+32-offset), 0, 3)
    elif fig == 'O':
        offset = 3
        thickness = 2
        d.ellipse((pos[0]*32+offset, pos[1]*32+offset, pos[0]*32+32-offset, pos[1]*32+32-offset), 0)
        d.ellipse((pos[0]*32+offset+thickness, pos[1]*32+offset+thickness, pos[0]*32+32-offset-thickness, pos[1]*32+32-offset-thickness), 255)
