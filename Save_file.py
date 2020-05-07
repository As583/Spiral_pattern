from tkinter import *
from turtle import *

#import cairosvg
#import canvasvg

def SaveEps():
    print('Saving in eps...')
    ts = getscreen()
    ts.getcanvas().postscript(file="Pattern.eps")

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