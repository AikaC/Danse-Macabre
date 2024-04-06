label start:
    scene Corridor
    show Chand at pendulum with dissolve
    show Bella childhappy2 at right with moveinright

    Ar "Look, mom! I’m flying!"

    show Eve angry at left with moveinleft
    Ev "Arabella Dummont! Get down right this instant!"
    Ar child sad "But, mom!" with dissolve

    Ev "You are to be the Duchess of these lands. I can’t have you risking injury."
    Ev "Get down. I won’t say it twice."
    Ar "Yes, mother."

    hide Chand with dissolve

    Ar child angry2 "My mom always says things like this. People may think she’s worried about me..."
    Ar "But all I can see is her concern for our family's reputation."
    Ev angry2 "Now, let’s begin your etiquette lesson. You seem to need it the most."
    Ev "How will a nobleman ask for your hand in marriage if you act this way?"
    Ar child angry "I don’t want to get married..."
    Ev angry "... For now. I’m sure you'll change your mind when the time comes."
    Ar child sad "If you say so…"

    hide Bella
    hide Eve with dissolve

    Ar "Well…"
    Ar "The time has come…"
    Ar "And I still don’t want to get married."

    scene Dinner with fade
    $point = 0

    Ad "...Bella? Arabella?"

    show Bella date happy2 with dissolve

    Ar "Yes? I'm sorry... I was lost in thought about the past."
    Ad date happy "Oh, sweetie… Are you nervous? I can understand."
    Ad date bored "Being around someone as magnificent as me can make ordinary people bashful."

    hide Bella with dissolve

    menu:
        "How should I respond? Do I please the archduke for political reasons?"
        "Smile shyly.":
            show Bella date happy2 with dissolve
            Ar "Of course..."
            $point += 1
            pass

        "“Actually, I found it boring.”":
            show Bella date bored2
            $point -= 1
            pass

    Ad date bored "So, dear Bella. May I call you Bella?"
    Ar date surprise "Actually-"
    Ad date bored "Wonderful. As I was saying, Bella…"
    Ad "I am quite certain you've heard about my past conquests, haven’t you?"
    Ar date happy2 "Oh, yes. I’ve heard that you have an impressive background."
    Ad date happy "More than impressive, in fact. The Luxembourg family has always been among the most noble."
    Ad "{i}I{/i}, of course, am not behind our name as {i}I{/i} acquired abilities worthy of envy."
    Ar date happy2 "It seems your life is always full of adventures."
    Ad date happy "Indeed. But, I'm curious, let me ask you… Are you the jealous type?"

    hide Bella

    menu:
        "Yes":
            $point -= 1
            pass
        "No":
            $point += 1
            pass

    show Bella date bored with dissolve

    Ad "I ask because it’s hard for ladies worldwide to resist someone as grand as myself."
    Ar date bored2 "Do you travel often?"
    Ad date happy "Yes, of course. Traveling is one of my passions."
    Ad "I know the finest places in this world."
    Ar date happy2 "You must have had wonderful experiences."
    Ad date happy "Not only me, but the people around me too, as wherever I go..."
    Ad date bored "... my presence alone transforms simple places into wonderful sceneries worthy of fairy tales."
    Ar date bored2 "You seem to have high self-esteem."

    hide Bella with dissolve

    menu:
        "Ignore his comments":
            $point += 1
            show Bella date happy2 with dissolve
            Ar "Speaking of transforming places, have you visited the art exposition downtown?"
            Ad date happy "Yes, I have."
            Ad date bored "I must admit, the art didn't impress me. They are not equal to my refined taste, of course."
            Ar date bored2 "Art is subjective, isn’t it? Maybe if you looked at it from another perspective…"
            Ad date bored "But frankly, I believe my discernment is superior to common folk."
            pass

        "Point out his flaws":
            $point -= 1
            show Bella date bored2 with dissolve
            Ar "With all due respect, Archduke, it's quite arrogant to assume your opinions matter the most."
            Ad date bored "Arrogant! Me?! How dare you?!"
            Ar date surprise "Just saying… Humility is a virtue valued by many."
            Ar "Maybe there's more to admire in someone who recognizes others' greatness."
            Ad date bored "Humility isn't expected from someone as important as an Archduke."
            Ar date bored2 "I believe it's best we end dinner here. Have a good evening, sir."
            pass

    hide Bella with dissolve
    jump travel
    return

label travel:
    scene Street with None
    show CarBody
    show WeelB
    show WeelF with dissolve

    Ar sbored2 "Curse that Archduke!"
    Ar "No way I am going to marry him!"

    show Paper with moveinleft
    Ar ssurprise "What is that?"

    menu:
        "Take the paper":
            hide Paper
            show Flyer
            pass

    Ar ssurprise "A... circus?"
    Ar "Maybe I could...?"
    Ar shappy2 "I better keep it for later... A small visit wouldn't hurt, would it?"

    scene Corridor with fade

    show Eve worry with dissolve

    Ev "So… How did it go?"

    show Eve worry2 with dissolve

    Ar ssurprise "The epitome of disaster."
    Ev worry "Please, try a bit harder. It'll be a blessing to our family if we create ties with the Luxembourg family."

    show Eve worry2 with dissolve

    Ar sbored2 "A blessing indeed."
    Ar "I'm going to my room to contemplate my future."
    Ar "Please, do not disturb me."

    hide Eve
    hide Bella
    show Flyer with fade

    Ar sworry "I wish I could have some fun…"

    jump circus

label circus:
    scene CircusOut with zoomout
    show Ring happy with dissolve

    Rm "Come and see! Come and see! The Shadow Circus from the Red Sea!"
    Rm "Take a bow and sit down, 'cause we just came into town!"

    Ar shappy2 "Now, this might be something!"
    Ar "Let's see what's inside..."

    hide Ring happy
    show Mage happy with pixellate

    Ma "Welcome to the Shadow Circus, where darkness reigns supreme!"
    Ma "Today we shall present our most mesmerizing act."
    Ma dance "Tell me, dear viewers, do you like to dance?" with dissolve
    Ma "For today, we shall showcase our play “Danse Macabre”."
    Ma "Are you ready to transport your mind to places beyond imagination?"
    Ma happy "Tonight, you are about to witness acts that defy reality..."
    Ma "… and uncover secrets as ancient as the shadows that surround us." with dissolve

    jump mageStart
label mageEnd:
    return
