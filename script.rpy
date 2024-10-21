
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
    
        scene black with dissolve
        jump chapter2
return

# SCENE 2
label chapter2:

    "Chapter 2"

    scene hallway
    "Miss Pauling and my steps echo in the empty hallway. We aren’t saying a word as we’re walking to the office she told me about."
    "She and I will spend most of our work hours in there. This will be my first time stepping in our office."
    "She probably has her mind in her other work-related things as she’s showing me around. I am not speaking simply because I am not told to, I hate small talk and because I don’t have any questions."
    "Honestly I don’t think I’d speak up even if I had any questions either… That’s a bad habit I need to get rid of. This job is important."
    "Miss Pauling and I stop in front of a lift. She presses a button and the doors open before us."
    scene lift

    show pauling neutral
    p "“Our office is pretty high up. The view is nice.”"
    a "“Allright.”"
    hide pauling

    scene office
    "After a little wait, the lift doors open and we’re greeted with a cozy atmosphere. Wooden furniture, dim lightning, windows to look outside."

    show pauling happy
    p "“I ordered you your very own work desk. I put it next to mine.”"
    p embarrassed "“We can … put it elsewhere if you wanna work in your own space.”"
    hide pauling

    menu:
        "Its current location is fine":
            jump current_location_is_fine

        "I wanna have a little space.":
            jump i_wanna_have_space

    return

    label current_location_is_fine:

    show pauling happy
    p "“Ah! Brilliant! Saves us time not needing to move it.”"
    p neutral "“Let’s get straight to work shall we?”"
    hide pauling

    jump choice3_done

    return

    label i_wanna_have_space:

    show pauling neutral
    p "“I totally understand. Please help me move your desk.”"
    p "“I’ll grab this end. You’ll grab the other.”"

    "I obey. We move my desk across the room. I will be working our backs facing each other."

    p "“Phew! Now we can get to work.”"
    hide pauling

    jump choice3_done

    return

    label choice3_done:

    "Miss Pauling carries a large pile of papers to me tells me to organise in chronological order. I eye the familiar typewriter font in the paper on top of the pile before setting it on my desk."
    "My eyes became tired as the hours went by."
    "I completed the sorting after a couple of more hours."
    a "“I’m done.”"
    show pauling doubt
    p "“Just a second.”"
    p neutral "“There.”"
    p "“Good job. I’m gonna take those from you and put them in folders. You can take a little break.”"

    show pauling surprised at left
    "She walked a few steps away from me with the pile. Her face lit up and she turned around."

    p "“There’s the mercenaries’ files in the 3rd locker of my desk. You can get to know the boys a little better by reading them."
    p embarrassed "“Some of their backgrounds may be a little weird. But you won’t mind, will you?”"
    a "“At least it’ll be an interesting legible.”"
    p neutral "“You’re right. I’ll go now. See you soon.”"

    "She presses the lift button with her elbow and leaves when the doors open. I’m surprised how easy she made carrying the papers look."
    hide pauling with dissolve

    "I stand up and rummage through the 3rd locker of Miss Pauling’s desk. I get my hands on a folder titled as the mercenaries’ files. It says “CLASSIFIED” in red on the middle."
    "My lips curl into a smile as I walk to my own desk. The classified text made the folder look very secret and important. I’m excited I have a pass that lets me get away with something a normal civilian wouldn’t."
    "A normal citizen would probably get assassinated for this."
    "I sat down, crossed my legs and prepared to dive into the mysteries of the folder. Which one should I read first?"

    default Demoman = False
    default Pyro = False

    menu:
        "Medic":
            jump Medic
            
        "Scout":
            jump Scout

        "Heavy":
                jump Heavy

        "Sniper":
            jump Sniper

        "Spy":
            jump Spy
            
        "Soldier":
            jump Soldier
            
        "Demoman":
            $ Demoman = True
            jump Demoman

        "Pyro":
            $ Pyro = True
            jump Pyro
            
        "Engineer":
            jump Engineer

    return

    label Medic:

    "I picked the BLU team doctor’s file first. It had the Medic’s black and white picture. He looked serious."

    a "{i}Oh. His real name is Ludwig. Hm. He definitely looks like a Ludwig.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "I blink and re-read the text in case my eyes were deceiving me the first time."
    "I chuckle out loud. No way this guy’s background is like a horror-themed sitcom."
    "I doubted if Medic’s qualified to be the team’s healer but I guess he is since he’s not been fired yet. He also did invent a ray that heals people in a short moment and a way to make them invincible for 8 seconds."
    "On second thought I wouldn’t fire him either. Even though he should’ve been locked up in an asylum 30 years ago…"
    jump file_choice_done
    return

    label Scout:
    "I picked the BLU team Scout’s file first. It had his black and white picture. He’s smiling."
    "This is the guy who complained about me being here."

    a "{i}Oh. His real name is Jeremy.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "The craziest part of his background is he having seven brothers. Oh, the poor mother of his not only gave birth but raised eight Scouts."
    jump file_choice_done
    return

    label Heavy:
    "I picked the BLU team’s Heavy weapons guy’s file first. It had his black and white picture. He looked serious."
    a "{i}Oh. His real name is Mikhail. That’s such a nice name. Gives me sympathetic vibes.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    a "{i}He’s from the USSR. That makes us neighbours.{/i}"
    "I can’t lie his story wasn’t exciting but it did make me frown."
    "I read the current description of him. It says he usually shows clear signs of enjoyment such as laughing when shooting people down. In addition, he treats his minigun as if it was sentient."
    "I shrug. I’m not weirded out by that. Good for him."
    jump file_choice_done
    return

    label Sniper:
    "I picked the BLU team Sniper’s file first. It had his black and white picture. He looked serious."
    a "{i}His real name is mister Mundy, I see…{/i}"
    "…"
    "Hmm. This one’s nothing crazy. An assassin so good at his job that even Admin became interested in hiring him."
    "I wonder why Miss Pauling warned me. Maybe the rest of the mercenaries are more mental."
    jump file_choice_done 
    return

    label Spy:
    "I picked the BLU team Spy’s file first. It had his black and white picture. He looked serious and wealthy type of guy."
    "His first and surname was stated but I don’t know how to pronounce them."
    "French is such a weird language compared to my own where every letter is pronounced the way it’s written and doesn’t play mind games like English and especially French."
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "Before I opened the Spy’s file, I had expected something crazy like Miss Pauling warned. He was just a hitman so good that even Admin became interested in hiring him."
    "I wonder why Miss Pauling warned me. Maybe the rest of the mercenaries are more mental."
    jump file_choice_done
    return

    label Soldier:
    "I picked the BLU team Soldier’s file first. It had his black and white picture. He was doing a salute with a serious face."
    "He’s chosen “Jane Doe” as his alias. I raise my brows confused."
    "An unidentifiable woman as an alias? Why? Maybe the rest of the file gives me an explanation."
    "There was his first and surname, age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "After reading the text I stare at it blankly. I shake my head and rub my temples processing all the information I just read with the two of my eyes."
    "Jesus Christ…"
    "I can see why Miss Pauling warned me before leaving."
    "I’m entertained by utterly mental stories but this one left me speechless."
    a "{i}All right… Let’s see the rest.{/i}"
    jump file_choice_done
    return

    label Demoman:
    "I picked the BLU team Demoman’s file first. It had his black and white picture. He looked sleepy."
    a "{i}Tavish Finnegan DeGroot. This is the first time hearing any of those names.{/i}"
    "Even though his first name was unfamiliar to me, it did amuse me. “Tavish” means a very normal or basic person in Finnish."
    "I’m hoping this coincidence isn’t foreshadowing anything."
    "The file had also stated his age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "I squint my eyes in disbelief. This text wants me to believe his eye is cursed by magic."
    "I need to ask Miss Pauling about this."
    jump file_choice_done
    return

    label Pyro:
    "I picked the BLU team Pyromaniac’s file first. It had the Pyro’s black and white picture."
    "There was age, height, weight and other medical information."
    a "{i}“First name: Unknown. Surname: Unknown.” How mysterious.{/i}"
    a "{i}“The subject has a neurological developmental disability: Semi-verbal autism.”{/i}"
    "That explains his muffling."
    "Now came the exciting part. -His background."
    "…"
    "The text and the evidence pictures gave me chills."
    "The burned victims had a terrified expressions plastered on their faces forever. Their skin was crusty and blackened."
    "The Pyro was known to show clear signs of enjoyment such as laughing and happily hopping around when burning people alive."
    "This guy is definitely a sadist."
    jump file_choice_done
    return

    label Engineer:
    "I picked the BLU team Engineer’s file first. It had his black and white picture. He was smiling with teeth."
    a "{i}Dell Conagher’s his real name.{/i}"
    a "{i}Dell… Dell… That’s such a nice name. No K’s or R’s or any other letters that make names sound blunt or harsh. “Dell” is perfectly soft.{/i}"
    a "{i}I have been wondering what to name my future cat or chihuahua. Now I know. If I ever get a pet that is…{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "I was highly impressed until the Gunslinger part."
    "Why the hell would one replace their fully functioning hand -and even the right one- for a robotic one?"
    "I shrug. He’s the one with 11 PhDs. Not me. Maybe he’s onto something. I really hope so for his sake…"
    jump file_choice_done
    return

    label file_choice_done:
    
    if Pyro:

        "I read more files. The stories got crazier and crazier. I admit I was very entertained so far."
        "I was surprised the Pyro being the only one whose real name was a mystery."
    else:
        "I read more files. The stories got crazier and crazier. I admit I was very entertained so far."
        
    "Now was the last file’s turn. The tank operator’s."
    a "{i}This is the guy who was a little too excited to see me. For a Finn too… Let’s see what’s this guy’s deal.{/i}"
    "I go through the text in a calm manner. I slowly start glaring at the text, scrunching up my nose and tightening my grip."
    "What a nutcase!"
    "I’m getting goosebumps. I was careful not to damage the paper even though I wanted to. I want nothing to do with anything regarding to this man."
    jump chapter3
    return

label chapter3: