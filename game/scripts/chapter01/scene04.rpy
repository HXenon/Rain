label chp01_scn04:
    #change scene

    """
    I stood up as I watched my surroundings which were full of students now empty.

    There was nothing but chairs neatly lined up. 

    The voices which had filled the room with laughter now gone,  not a laugh to be heard.

    All I could hear was just my breath and the sound of friction from my clothes. 

    """

    
    "I picked up my book which had been used as a pillow for my arms to rest on, store it in my bag, and left the classroom."

    #change scene
    with fade

    """
    I walked along the hallway filled with puddles of water.

    Watching my steps and carefully walking so to not slip. 

    The cold breeze scattered my hair around.

    It's normally hot here, but when it rains, the air get really cold.

    """
    
    #chnage scene
    with fade

    """
    I met up with him at the gates and we head home–

    Together.

    """

    #change scene
    with fade

    "The streets were empty, {w=0.2} a normal sight if you've lived here for a long time."

    with fade

    Ren "{cps=2}...{/cps}"

    "?" "{cps=2}...{/cps}"

    """
    Not a single word came out of our mouths.

    Reason was because We don't really get along much.

    The only reason we were walking home together was because our homes are in the same direction.

    Of course, we could just walk by ourselfs instead.

    I don't remember when it started but we ended up walking home together since a while ago.

    It became a routine for us, so we just went along with it.
    
    """
    
    #change scene
    with fade

    "Time passed, before I knew it, it was time to part ways."

menu :

    "See you–":
        jump say_goodbye01

    "...":
        jump edgy01

    #say partings
label say_goodbye01 :

    Ren "See you–"
    jump alone01

    #doesn't do anything
label edgy01 :

    Ren "{cps=2}...{/cps}"
    jump alone01


label alone01 :

    "I raised my arm as to say goodbye, held it there for a while then lowered it down slowly."

    "Alone."

    "Again."

    #change scene to home

    """
    Arriving at my home, I took my keys and opened the door.

    Clack*

    The sound of the door lock opening, echoed. 

    No one was there– {w=0.5}as usual.

    I entered my room, 
    {w=0.5}put my bag down, 
    {w=0.5}and lay on my bed. 

    I had been blinking every other seconds, with each blinks getting slower and slower. 
    
    Until finally–

    My eyelids gave.
   
    """

    #not quite sleeping
    """
    Ch*
    
    A feint sond

    Chk*

    A very familiar sound.

    Tchk*

    One which I had heard many times over my life.

    Tchk*

    The sound of a clock ticking which accompanied my sleep.

    Tchak*
    
    """

    #PROLOGUE ENDS

    jump ending