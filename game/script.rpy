# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Eileen")


# The game starts here.

label monologue01 :
    scene bg sea

    "Rain."

    """
    The sound of water trickling down, {p}drowning out the voice in the class.

    Each droplet of water creates a sound-like melody– 
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

    As time passes 
    {w}by.

    As the rain 
    {w}pours down.

    As the voices 
    {w}echoed.
    """"

    with Fade(0.5, 1.0, 0.35)

    "..."

    with Fade(0.75, 1.0, 0.4)
    "..."

    with Fade(0.1, 1.5, 0.5)

    "."


    # closed eye scene
    scene bg black

    """"

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

    "-wake up"

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

    Ren "..."

    "?" "What's with the face?"

    Ren "..."

    "?" "What? Gonna cry? Want me to call mommy to comfort her dear little baby? Uhuu–"

    Ren "Fuck off.."

    "?" "What was that?"

menu :

    "I said FUCK OFF!"
        jump fight_back :

    "Nothing."
        jump do_nothing :

label fight_back :

    "There's no way I'm saying that!"
        jump do_nothing

label do_nothing :

    Ren "Nothing."

    "?" "Man, you're boring."

    "?" "Hurry and sort your stuff out, I'll be at the gates."

    Ren "..."

    """"

    He left.

    I sat there trying to calm myself down.

    """
    # change scene

    "It was quite"

    Ren "Looks like the rain had stopped"

    







    
    """

    """
    # This ends the game.

    return
