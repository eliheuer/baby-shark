# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,64

# DRAWS A GRID
def grid():
    stroke(1,0,0,0.5)
    strokeWidth(1)
    rect(M, M, W-(M*2), H-(M*2))
    stpX, stpY = 0, 0
    incX, incY = M/2, M/2
    for x in range(29):
        polygon((M+stpX, M),
                (M+stpX, H-M))
        stpX += incX
    for y in range(13):
        polygon((M, M+stpY),
                (W-M, M+stpY))
        stpY += incY

# REMAP INPUT RANGE TO VF AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan  = inputMax  - inputMin   # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# NEW PAGE
def new_page():
    newPage(W, H)
    #frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
new_page()
font("../../fonts/Baby-Shark.ttf")
#grid() # Toggle for grid view
fill(1)
stroke(None)
fontSize(M*1.3)
text("ABCDEFGHIJKLMNO", (M*2.5, M*5))
text("PQRSTUVWXYZ 1234", (M*2.5, M*4))
text("567890-–—&!?$£ (.,;:)", (M*2.5, M*3))
text("3D-RENDER 512 GTL", (M*2.5, M*2))

stroke(1)
strokeWidth(2)
line((M*2.5, H-M), (W-(M*2.5), H-M))
line((M*2.5, M), (W-(M*2.5), M))
font("Helvetica")
fontSize(24)
stroke(None)

text("Baby Shark v0.1", (M*2.5, H-(M*1.5)))

text("4.4k", (W-M*3.25, H-(M*1.5)))

text("OFL v1.1", (W-M*4, (M*1.15)))

text("Designed and Engineered by Eli Heuer", (M*2.5, (M*1.15)))

saveImage("specimen-001.png")
print("Drawbot: Done :-)")
