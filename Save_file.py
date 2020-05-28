import turtle

#import cairosvg
#import canvasvg

def SaveEps(file_name):
    print('Saving in eps...')
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=file_name+'.eps')

# TODO: Настроить сохранение в формате PNG
'''
def SavePNG():
    print('Saving in png...')
    ts = getscreen().getcanvas()
    canvasvg.saveall('tmp.svg', ts)
    with open('tmp.svg') as svg_input, open('newduck.png', 'wb') as png_output:
        cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    shutil.rmtree(tmpdir)  # clean up temp file(s)
'''