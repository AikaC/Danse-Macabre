################################################################################
## Quick Time com barra
################################################################################
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script


screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.

label mageStart:
    $ time = 3                                     ### set variable time to 3
    $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_jump = 'menu_slow'                    ### set where you want to jump once the timer runs out
    $point = 0
    Ar shappy "To win the game, you must click on the right options to increase the 'fear level'."
    Ar ssurprise "Watch out for the time limit!"

    show screen countdown                          ### call and start the timer
    menu:
        "{font=PARCHM.TTF} {size=+50}Question One\:{/font=PARCHM.TTF} {/size} Who is the author of the book \"Frankenstein\"?"

        "Jane Austen":
            jump js_mage01
        "Mary Shelley":
            Ar shappy "Ha! That was easy..."
            $point += 1
        "Charlotte Bronte":
            jump js_mage02
hide screen countdown
label mageQ2:
    show screen countdown                          ### call and start the timer

    menu:
        "{font=PARCHM.TTF} {size=+50}Question Two\:{/font=PARCHM.TTF} {/size} What is the name of Victor Frankenstein's creature?"

        "Frankenstein":
            jump js_mage01
        "The monster":
            Ar sbored "I remember reading about that! The monster didn't have a name..."
            $point += 1
        "Thing":
            jump js_mage02
hide screen countdown
label mageQ3:
    show screen countdown                          ### call and start the timer

    menu:
        "{font=PARCHM.TTF} {size=+50}Last question\:{/font=PARCHM.TTF} {/size} Who is the protagonist of Frankenstein?"
        "The monster":
            jump js_mage01
        "Elizabeth":
            jump js_mage02
        "Victor Frankenstein":
            Ar shappy "I knew it!"
            $point += 1
            jump mageEnd
hide screen countdown
label js_mage01:
    Ma "Behold, the dance of shadows, where reality blurs and dreams take flight."
    return

label js_mage02:
    Ma "Witness as the darkness itself becomes my canvas, painting scenes of wonder and terror for your entertainment."
    return
label menu_slow:
    Ma "Hmm too slow, let's try again."
    jump mageStart