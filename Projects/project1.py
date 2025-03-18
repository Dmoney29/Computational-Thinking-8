###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
############################################### 

stage.set_background("winter")
q1 = codesters.Square(100, 100, 200, 'white')
q2 = codesters.Square(-100, 100,200, 'pink')
q3 = codesters.Square(-100, -100, 200, 'white')
q4 = codesters.Square(100, -100, 200,'pink')

s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite ("BASKETBALL",-100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("jordans", 100, -100)
s3.set_size(1.0)
s4 = codesters.Sprite("headphones", -100, 100)
message1 = codesters.Text ("Dallas Lael Dixon",0,220,"white")
message2 = codesters.Text("Philppians 4:13",0,-220,"black")