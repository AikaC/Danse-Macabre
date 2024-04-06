#Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ar = Character("Arabella", image = 'Bella')
define Ev = Character("Evellyn", image = 'Eve')
define Ad = Character(_("Archduke"), image = 'Bella')
define Rm = Character(_("Ringmaster"), image = 'Ring')
define Ma = Character(_("Magician"), image = 'Mage')

# Declare image used for each character

#BG
image Corridor = "BG/Corridor.jpg"
image Dinner = "BG/Dinner.jpg"
image Street = "BG/Street.jpg"
image CircusOut = "BG/CircusOut.jpg"

#Sprites
image Chand = "Sprites/Chandelier.png"
image Paper:
 "Sprites/Carriage_paper.png"
 xalign 0.47 yalign 0.38

image CarBody:
 "Sprites/Carriage_Body.png"
 xalign 0.5 yalign 0.3
 pause 0.6
 linear 0.1 yalign 0.25
 linear 0.1 yalign 0.3
 pause 0.3
 repeat

image WeelB:
 "Sprites/Carriage_WB.png"
 xalign 0.06 yalign 0.9
 linear 5.0 rotate 90
 linear 5.0 rotate 180
 linear 5.0 rotate 360
 linear 5.0 rotate 90
 repeat

image WeelF:
 "Sprites/Carriage_WF.png"
 xalign 0.8 yalign 0.9
 linear 5.0 rotate 90
 linear 5.0 rotate 180
 linear 5.0 rotate 360
 linear 5.0 rotate 90
 repeat

image Flyer:
 "Sprites/Flyer.png"
 xalign 0.5 yalign 0.5

#Arabella
image Bella child angry = "Bella/Bella child angry.png"
image Bella child angry2 = "Bella/Bella child angry2.png"
image Bella child sad = "Bella/Bella child sad.png"
image Bella child happy = "Bella/Bella child happy.png"
image Bella childhappy2 = "Bella/Bella childhappy2.png"

image side Bella sbored = im.Scale("Bella/Bella date bored.png", 319, 366, xoffset=80, yoffset=0)
image side Bella sbored2 = im.Scale("Bella/Bella date bored2.png", 319, 366, xoffset=80, yoffset=0)
image side Bella shappy = im.Scale("Bella/Bella date happy.png", 319, 366, xoffset=80, yoffset=0)
image side Bella shappy2 = im.Scale("Bella/Bella date happy2.png", 319, 366, xoffset=80, yoffset=0)
image side Bella ssurprise = im.Scale("Bella/Bella date surprise.png", 319, 366, xoffset=80, yoffset=0)

image Bella date bored:
 "Bella/Bella date bored.png"
 xalign 0.5 yalign 0.3

image Bella date bored2:
 "Bella/Bella date bored2.png"
 xalign 0.5 yalign 0.3

image Bella date happy:
 "Bella/Bella date happy.png"
 xalign 0.5 yalign 0.3

image Bella date happy2:
 "Bella/Bella date happy2.png"
 xalign 0.5 yalign 0.3

image Bella date surprise:
 "Bella/Bella date surprise.png"
 xalign 0.5 yalign 0.3

#Evellyn
image Eve angry = "Eve/Eve angry.png"
image Eve angry2 = "Eve/Eve EyesClosed.png"
image Eve worry = "Eve/Eve worry.png"
image Eve worry2 = "Eve/Eve worry2.png"

#Ringmaster
image Ring happy = "Circus/Ring happy.png"

#Mage
image Mage happy = "Circus/Mage happy.png"
image Mage dance = "Circus/Mage dance.png"

# Declare custom ATL and transitions

# Define the rotation animation.
transform pendulum:
    block:
        xalign 0.5 yalign -0.3
        linear 1.0 rotate 15.0
        linear 1.0 rotate 0.0
        linear 1.0 rotate -15.0
        linear 1.0 rotate 0.0
        repeat