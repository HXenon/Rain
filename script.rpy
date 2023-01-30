# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sea

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

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

    "Ren" "I’ll be using you as a wall, 
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

    ...

    ...

    .





    
    """


    # This ends the game.

    return
