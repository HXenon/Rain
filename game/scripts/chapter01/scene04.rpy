label chp01_scn04:
    #change scene

    g """
    {clear}

    I stood up as I watched my surroundings which were full of students now empty.

    There was nothing but chairs neatly lined up. 

    The voices which had filled the room with laughter now gone,  not a laugh to be heard.

    All I could hear was the sound of my breath and my clothes brushing my skin. 
    
    I picked up my book which had been used as a pillow for my arms to rest on, store it in my bag, and left the classroom.
    """


    #change scene
    with fade

    g """
    {clear}

    I walked along the hallway filled with puddles of water.

    Watching my steps and carefully walking so to not slip. 

    The cold breeze scattered my hair around.

    It's normally hot here, but when it rains, the air gets really cold.
    
    {clear}
    """
    
    #chnage scene
    with fade

    """
    I met up with him at the gates and we head home.

    Together.
    """

    #change scene
    with fade

    "The streets were empty,{w=0.2} a normal sight to see if you've been here long enough."

    with fade

    Ren "{cps=2}...{/cps}"

    "?" "{cps=2}...{/cps}"

    """
    Not a single word came out of our mouths.

    We've never really gotten along anyway.

    The only reason we were walking home together was because our homes are in the same direction.

    Of course, we could just walk by ourselves instead.

    I don't exactly remember when it started but we ended up walking home together quite a while ago.

    It had became a routine for us, so we just went along with it.
    """
    
    #change scene
    with fade

    "Time passed, and before I knew it, it was time to part ways."

    menu .say_goodbye:
        "See you around.":
            jump .say_goodbye_1

        "...":
            jump .say_goodbye_2

    #say partings
    label .say_goodbye_1:
        "I raised my arm to say goodbye, held it there for a while then slowly lowered it down."
        Ren "See you around."
        jump .alone

    #doesn't do anything
    label .say_goodbye_2:
        Ren "{cps=2}...{/cps}"
        "There he goes."
        jump .alone


    label .alone :
        """
        Alone.{w}\nAgain.
        """

    #change scene to home

    """
    Arriving at my home, I took my keys and opened the door.

    Clack*

    The sound of the door lock opening, echoed. 

    No one was there, {w=0.5}as usual.

    I entered my room, 
    {w=0.5}put my bag down, 
    {w=0.5}and lay on my bed. 

    I had been blinking every other seconds, with each blinks getting slower and slower. 
    
    Until finally,

    My eyelids gave in.
   
    """

    #not quite sleeping
    """
    Ch*
    
    That faint sound,

    Chk*

    That very familiar sound.

    Tchk*

    One which I had heard many times over my life.

    Tchk*

    The sound of a clock ticking which accompanied my sleep.

    Tchak*
    
    """

    #PROLOGUE ENDS

    jump ending