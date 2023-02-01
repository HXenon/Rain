# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Ren")


# The game starts here.

label start :
    scene bg sea

    "Rain."

    """
    The sound of water trickling down, {p}drowning out the voice in the class.

    Each droplet of water creates a melody-like sound, 
    {p}calming, 
    {w} more than any song I have ever heard.


    It was almost time to go home.
    
    It was the last class of the day.

    It was 
    {w}noisy.

    Students were talking left and right, I couldn’t seem to focus on anything. 

    All I could hear, was just water pouring down.

    The rain was 
    {w}loud.

    Had someone talked to me, I wouldn’t be able to hear a thing of what they would say.
    
    No one’s going to talk to me either way.

    I’m not very noticeable in the class.

    I don’t really talk to anyone much.

    I’m just another student amongst the class–

    """

    #change scene night sky for now cause i dont have any assets yet

    scene bg night
    with Fade(0.5, 1.0, 0.35)
    """

    My eyes felt 
    {w}heavy.

    """
    with Fade(0.5, 1.0, 0.35)
    """

    My eyelids kept falling down each time I try to pull them up.

    My body felt imbalanced.

    Going in an up and down motion, as if agreeing to something.

    """
    with Fade(0.5, 1.0, 0.35)
    """
    It felt as I’m about to fall at any point.

    Falling down would probably hurt.

    It’d also attract a lot of attention.

    I wouldn’t want that.

    """

    # change scene
    """
    
    I rested my chin on my arms.

    It wasn’t a very comfortable position, but it keeps me from falling down.

    Fortunately, I’m seated far from the front, just behind someone with a bigger stature.
    
    """

    Ren "I’ll be using you as a wall, 
    {w}hope you won’t mind." 

    
    #change scene
    """
    I stared at the clock in front of me which had been conveniently placed above the blackboard. 

    It was placed there for the students to keep track of the time.

    The teachers would often go past the lesson time and so the students would remind the teachers that it was time.

    Although, some teacher would just get annoyed and it would end up being a longer lecture for us.

    """

    with Fade(0.5, 1.0, 0.35)
    #change scene
    """

    I followed the arrow head as it ticks around.
    
    Each ticks tells the seconds passing.
    
    Each tick felt slower than the ticks before.
    
    Each tick pulled me closer to the world of dreams.

    Everything started to squiggle around.
    
    If I were to describe it, 
    {w}it would feel as if I am drunk.
    {p}Not that I would know what being drunk feels like.

    My eyes which had been blinking every second started to 
    {w}blink slower.

    My consciousness slowly 
    {w}fades away.
    """
    with Fade(0.5, 1.0, 0.35)

    """
    As time passes 
    {w}by.

    As the rain 
    {w}pours down.

    As the voices 
    {w}echoed.
    
    """

    with Fade(0.5, 1.0, 0.35)

    "..."

    with Fade(0.75, 1.0, 0.5)
    "..."

    with Fade(1.0, 1.5, 1.5)

    "."


    # closed eye scene
    scene bg black

    """

    It was dark, but it’s different than that of a unlit closed room.

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

    I felt calm— 
    {w}no, 
    {w}relieved. 

    The more thoughts that popped up, the more 
    {w}relieved I got. 

    """

    # ren wakes up

    "?" "–up."

    "shake*"

    "?" "-wake up"

    "shake*"

    "?" "–wake UP, HOO–Y!"

    """

    A loud sound had pierced through my eardrums.

    Like a gunshot, 
    {w}piercing trough.

    It had inevitably woke me up.

    """

    Ren "Agh!"

    "?" "Finally!"

    Ren ".{w=0.5}.{w=0.5}."

    "?" "What's with the face?"

    Ren ".{w=0.5}.{w=0.5}."

    "?" "What? {w=1.0}Gonna cry? {w=1.0}Want me to call mommy to comfort her dear little baby? {w=1.0}Uhuu–"

    Ren "Fuck off.."

    "?" "What was that?"

menu :

    "I said FUCK OFF!":
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
    # change scene

    "It was quite"

    Ren "Looks like the rain had stopped."

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

    Ren ".{w=0.5}.{w=0.5}.{w=0.5}"

    "?" ".{w=0.5}.{w=0.5}.{w=0.5}"

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
        jump do_nothing02

    #say partings
label do_goodbye01 :

    Ren "See you–"
    jump alone01

    #doesn't do anything
label do_nothing02 :

    Ren "..."
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




    # This ends the game.

    return
