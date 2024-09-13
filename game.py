'''
World of CodeCraft is a command line text adventure game written in Pyhton by Caique Fabris and Lou Espiral.
'''

import classes

prisoner_lines = [
    'Wow!',
    'Hi!',
    'Bye!'
]
prisoner = classes.NPC('Prisoner', prisoner_lines)

classes.data.location_list[0][3] = [prisoner]


# Create the world and the hero
game = classes.Game()
world = classes.World()
bestiary = None
hero = classes.Hero(current_location=world.locations[0])
world.locations[0].visited = True

# Display initial text
game.slow_print(classes.data.welcome)
game.slow_print(classes.data.help_text)
game.slow_print(classes.data.intro)
hero.look(game)
game.choice(hero, world)