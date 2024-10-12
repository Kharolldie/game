
define p = Character("Miss Pauling", color="#A03DE9", image='pauling')
define a = Character("Miss Ahmavaara", color="#6918a3")
define t = Character("The tank operator", color="#97b7c6", image='tank')
define q = Character("???", color="#ffffffff")

# SCENE 1
label start:

    scene hallway with fade

    "Today is the first day in my new workplace. Miss Pauling, who I've met just five minutes ago, is taking me to meet the mercenaries."

    show pauling neutral
    p "Are you nervous, Miss Ahmavaara? I know you've just been kinda kidnapped, put in a new uniform, met me and now you have to meet nine more people, but this will be the least stressful day you'll have from now on."
   
    p sad "Sorry to be this depressing from the start. But Administrator expects a lot from both of us."

    a "I did sign up for this."

    p neutral "You're right."

    show pauling at left
    p "Oh! We're here!"

    "The hallway has led us to a door. Ruckus can be heard behind it. I resist the urge to roll my eyes and sigh in discomfort in front of Miss Pauling. She opens the door and the racket of grown men fills my eardrums."
    hide pauling

    scene conference room with fade
    q "C'mon, fellas. Shut up!"

    q "I WILL SHUT A BOX WITH YOUR ASS IN IT AND KICK IT DOWN THE STAIRS!"

    q "SHUT MOUTHS!!!"

    "The whole room becomes dead silent thanks to this guy. Thank God there's someone tolerable in this team."

    show pauling neutral
    p "I've gathered you all here to introduce you my new colleague Miss Ahmavaara."

    a "Pleasure to be working with you."

    hide pauling
    "Someone made an audible gasp. Each of the men turned around to look at the guy sitting in the very back row. They looked at him surprised. Like it would be the 7th miracle of the blonde guy in the back to make any noices."
    
    show tank embarrassed
    q "..."

    "He seemed to regret drawing attention to him. He looked at me again."

    q "You’re Finnish?"

    "I could tell from his rally English alone he was one too."
    hide tank
    menu:

        "Yes.":
            jump choice1_yes

        "I will not disclose personal information.":
            jump choice1_i_will_not

        "Why are you asking?":
            jump choise1_why

    return

    label choice1_yes:
        show tank happy
        q "Me too!"
        show tank embarrassed
        q "Anyway… Go on. I’ll stop talking."
        hide tank

        jump choice1_done

    label choice1_i_will_not:
        show tank sad
        q "Sorry."

        "He looks at the floor and stops the interruption."
        hide tank

        jump choice1_done

    label choise1_why:
        show tank embarrassed
        q "Just curious."

        "I can tell he’d give a longer and detailed explanation why if he wasn’t under eleven people’s curious eyes."
        hide tank

    label choice1_done:

        "I was introduced and the men were told I would be doing half of Miss Pauling’s work. I would be in contact to them every now and then."
        
        "The youngest of the lot voiced his complaints about that. I already dislike him…"
        scene hallway with fade
        "The conference was over and I started walking away from the room with Miss Pauling as the men were getting up from their chairs."

        "My name is called behind us. The speaker translated my title into my native language."
        show tank neutral
        q "Neiti Ahmavaara?"

        "Miss Pauling and my eyes were round out of surprise. This man probably came to tell me something he was too shy to say at the conference now that we were alone. -Almost alone."
        
        show pauling at left: 
            pos (0.0, 0.2) anchor (0.0, 0.0)

        p doubt "Would you like to speak with him alone?"
        hide pauling
        hide tank
    menu:

        "Yes.":
            jump choice2_yes
        
        "I’d prefer if you stayed with me.":
            jump choice2_id_prefer



    label choice2_yes:
        show pauling neutral
        p "All right. I’ll wait for you by the exit."
        hide pauling with dissolve

        "She starts walking away."

        show tank doubt
        q "..."

        "The moustache man watches carefully as the rest of the mercenaries walk past us. Some of them walked slowly on purpose in case they could hear what he was about to say."
        "When he made sure they were far enough, he spoke to me in Finnish."

        show tank happy
        q "Tereve, tereve! Mie halusin vaa sannoo, et on tosi mukava, et täälo toone suamalaine. Voiv vihroin puhhuu ommaa äirinkiältä."

        "I squint my eyes as if that’d help me understand his God forsaken dialect. I reply with proper finnish."

        a "(Please speak in written language. I don’t understand a single word you’re saying.)"

        show tank surprised
        q "(Oh! I’m sorry. Is this better?)"

        a "(Yes. Now start over, please.)"

        show tank happy
        q "(I said I just wanted to say it’s so nice that there’s another Finn. I can finally speak my native language.)"

        a "(Don’t get too used to it. We won’t be talking that much.)"

        show tank neutral
        q "(I know. You’ll be really busy.)"
    
        show tank happy
        q "(I’m the Tank operator by the way. You can call me Tank like everyone does.)"

        "He offers me his hand. I shake it. It’s hot and a tad sweaty."

        a "(You probably won’t need another introduction from me?)"

        show tank
        t happy "(No. I already remember your name better than my colleagues’.)"

        "I raise my brows at him."

        t neutral "(You must be busy. I just wanted to introduce myself and tell you how happy I am that you’re here. I’ll talk to you later, allright?)"

        a "(Mhm.)"

        hide tank with dissolve
        "I watched quietly as he walked away."
        "I walked to the exit and met up with Miss Pauling. I’m relieved she didn’t look curious."

        jump choice2_done




    label choice2_id_prefer:

        show pauling neutral
        p "Okay."
        
        show pauling at left:
            pos (0.0, 0.2) anchor (0.0, 0.0)

        show tank embarrassed
        "I’m sure the man wanted to talk to me alone since he doesn’t seem to like audience. But I need to follow Miss Pauling. I would be lost in the building and didn’t know where to go next if she left."

        hide pauling

        show tank doubt
        q "..."

        "The moustache man watches carefully as the rest of the mercenaries walk past us. Some of them walked slowly on purpose in case they could hear what he was about to say."
        "When he made sure they were far enough, he spoke to me in Finnish."

        show tank happy
        q "Tereve, tereve! Mie halluusin vaa sannoo, et on tosi mukava, et täälo toone suamalaane. Voiv vihroin puhhuu ommaa äirinkiältä."

        "I squint my eyes as if that’d help me understand his God forsaken dialect. I reply with proper finnish."

        a "(Please speak in written language. I don’t understand a single word you’re saying.)"

        show tank surprised
        q "(Oh! I’m sorry. Is this better?)"

        a "(Yes. Now start over, please.)"

        show tank happy
        q "(I said I just wanted to say it’s so nice that there’s another Finn. I can finally speak my native language.)"

        a "(Don’t get too used to it. We won’t be talking that much.)"

        show tank neutral
        q "(I know. You’ll be really busy.)"
    
        show tank happy
        q "(I’m the Tank operator by the way. You can call me Tank like everyone does.)"

        "He offers me his hand. I shake it. It’s hot and a tad sweaty."

        a "(You probably won’t need another introduction from me?)"

        show tank
        t happy "(No. I already remember your name better than my colleagues’.)"

        "I raise my brows at him."

        t neutral "(You must be busy. I just wanted to introduce myself and tell you how happy I am that you’re here. I’ll talk to you later, allright?)"

        a "(Mhm.)"
        
        hide tank with dissolve
        "Miss Pauling and I watched quietly as he walked away. I’m relieved my female colleague didn’t look curious."


        jump choice2_done

    label choice2_done:
        show pauling neutral
        p "Ready to continue? Good."
        hide pauling with dissolve
        "We exit the building together. Now that the mercenaries know I exist, it was time for me to learn the timetables, tech and maps."
    


    # Scene 1 end

# SCENE 2
    
    
    scene black with fade

    "Chapter 2"

    
    # This ends the game.

    return
