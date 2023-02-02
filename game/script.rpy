# "Rain" a visual novel


#region Game Configurations
init python:
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

transform triple_zoom:
    zoom 3.0
#endregion


#region Character Declarations
define g = nvl_narrator
define Ren = Character("Ren")
#endregion


# Start the game
label start:
    jump chp01_scn01

# End the game
label ending:
    scene bg black with Dissolve(2.0)
    return
