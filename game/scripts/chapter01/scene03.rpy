label chp01_scn03:
    scene bg black
    with Fade(1.0, 1.75, 1.5)

    """
    It was dark, but it's different than that of a unlit closed room.

    I could hear faint sounds in the background.

    Sounds of the rain.

    Sounds of my classmates talking.

    Sound of my own breathing.

    Moments had passed. 

    How long has it been? 

    Has the school ended?

    Should I go home?

    Will there be someone waiting for me at home?

    Thoughts kept popping up with questions upon questions.

    I felt calm—{w} no,{w} relieved. 

    The more thoughts that popped up,{w} the more relieved I got. 
    """

    # ren wakes up

    "?" "–up."

    "*shake*"

    "?" "-wake up"

    "*shake*"

    "?" "–wake UP,{w=0.5}{nw}{done} OOI!"

    show bg glasswindow
    with hpunch

    "?" "–wake UP,{fast} OOI!"

    """
    A loud sound had pierced through my eardrums.

    Like a gunshot,{w} piercing trough.

    It had inevitably woken me up.
    """

    Ren "Agh!"

    "?" "Finally!"

    Ren "{cps=2}...{/cps}"

    "?" "What's with the face?"

    Ren "{cps=2}...{/cps}"

    "?" "What? {w=1.0}Gonna cry? {w=1.0}Want me to call mommy to comfort her dear little baby? {w=1.0}{cps=*0.2}Uhuu–{/cps}"

    Ren "{size=-14}Fuck off...{/size}"

    "?" "What was that?"

menu :
    "I said, FUCK OFF!":
        jump fight_back

    "Nothing.":
        jump do_nothing

label fight_back :
    "There's no way I'm saying that!"
    jump do_nothing

label do_nothing :
    Ren "Nothing."

    "?" "Man, you're boring."

    "?" "Hurry and sort your stuff out, {w=1.0 }I'll be at the gates."

    Ren "..."

    """
    He left.

    I sat there trying to calm myself down.
    """
    
    scene bg night
    with Fade(0.25, 0.5, 0.25)

    "It was quiet."

    Ren "Looks like the rain had stopped."

    scene bg black
    with Dissolve(1.0)

    jump chp01_scn04