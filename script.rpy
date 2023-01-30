# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

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

    Students were talking left and right,
    {w}I couldn’t seem to focus on anything. 

    All I could hear, was just water pouring down.

    The rain was 
    {w}loud.

    Had someone talked to me I wouldn’t be able to hear a thing of what they would say.
    {p}No one’s going to talk to me either way.

    I’m not very noticeable in the class.

    I don’t really talk to anyone much.

    I’m just another student amongst the class–
    
    """


    # This ends the game.

    return
