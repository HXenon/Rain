# "Rain" a visual novel

#region Game Configurations

#endregion


define g = nvl_narrator
define Ren = Character("Ren")

#endregion


# Start the game
label start:
    jump chp01_scn01
    

# End the game
label ending:
    return
