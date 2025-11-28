# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mike", image = "mike")
image mike:
    animation
    "images/mike1.png"
    yalign 0.5
    easeout 0.3 yalign 0.25
    easein  0.3 yalign 0.5

screen Stats:
    text "Dobre: [good]" xpos 0.1 ypos 0.1
    text "Złe: [bad]" xpos 0.3 ypos 0.1

init python:
    import os
    import random
    current_path_saute = os.getcwd()
    current_path = current_path_saute.replace("\\", "/")
    def get_random_pierd():
        pierd_path = current_path + "/game/images/pierd/"
        pierds = [f for f in os.listdir(pierd_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        return os.path.join(pierd_path, random.choice(pierds))
    def get_random_pyszne():
        pyszne_path = current_path + "/game/images/pyszne/"
        pysznes = [f for f in os.listdir(pyszne_path) if f.endswith(('.jpg', '.jpeg', 'png', '.gif'))]
        return os.path.join(pyszne_path, random.choice(pysznes))

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg road

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mike
 
    # These display lines of dialogue.

    m "Cześć, jestem Mike."

    m "Chcesz ze mną zagrać w grę?"

    menu:
        "Tak":
            jump game
        "Nie":
            return

    # This ends the game.

    return

label game:
    scene bg road
    show mike
    m "Wspaniale!"
    m "Będę pokazywał Ci obrazki i powiedz tylko czy Ci się podobają, czy też nie"
    m "Dźwięki będą Ci podpowiadać, czy Twój wybór jest dobry czy nie"
    m "Określ ile błędów będziesz mógł popełnić:"
    python:
        avail_bads_string = renpy.input("Ilość możliwych błędów: ", length=3)
        avail_bads = int(avail_bads_string)
    m "Jeśli będziesz już gotowy wybierz tak i zaczynamy..."
    menu:
        "Tak":
            jump ready
        "Nie":
            jump start
label ready:
    hide mike
    $ good = 0
    $ bad = 0
    while bad < avail_bads:
        $ random_pierd = get_random_pierd()
        image random_pierd:
            random_pierd
            zoom 0.5
        show random_pierd
        m "Podoba Ci się?"
        menu:
            "Tak":
                $ good +=1
                play sound "audio/goodresult.mp3"
            "Nie":
                $ bad +=1
                play sound "audio/error.mp3"
        hide random_pierd

        $ random_pyszne = get_random_pyszne()
        image random_pyszne:
            random_pyszne
            zoom 0.5
        show random_pyszne
        m "Podoba Ci się?"
        menu:
            "Tak":
                $ bad +=1
                play sound "audio/error.mp3"
            "Nie":
                $ good +=1
                play sound "audio/goodresult.mp3"
        hide random_pyszne

    jump end

label end:
    scene bg road
    show mike
    show screen Stats
    m "Oto Twoje wybory"
    m "Chcesz zagrać ponownie?"
    menu:
        "Tak":
            hide screen Stats
            jump game
        "Nie":
            return     
