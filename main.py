from spaceplayer import SpacePlayer
from shipmap import World
import spaceenemies
import parse
from textwrap import fill
from textwrap import dedent

from terminalsize import get_terminal_size

debug_mode = True
def play():
    clear_screen()
    print("Escape from USS Callister!")
    world = World()
    spaceplayer = SpacePlayer()
    print_wrap(world.tile_at(spaceplayer.x,spaceplayer.y).intro_text())
    while True:

        [raw_input, parsed_input] = parse.get_command()
        if(parsed_input):
            if(len(parsed_input)==1):
                if(parsed_input[0] == "help"):
                    print_wrap(help_text)
                elif(parsed_input[0] == "check"):
                    print_wrap(world.tile_at(player.x,player.y).intro_text())
                elif(parsed_input[0] == "exit" or parsed_input[0] == quit):
                    exit()
                else:
                    print("I don't understand what you are trying to do. Please try again.")
            elif(len(parsed_input) == 2):
                if(parsed_input[0] == "go"):
                    move_status = False
                    if(parsed_input[1] == "forward"):
                        [move_status, move_description] = world.check_forward(spaceplayer.x, spaceplayer.y)
                        print_wrap(move_description)
                        if(move_status):
                            spaceplayer.move_forward()
                    elif(parsed_input[1] == "back"):
                        [move_status, move_description] = world.check_back(spaceplayer.x, spaceplayer.y)
                        print_wrap(move_description)
                        if(move_status):
                            spaceplayer.move_back()
                    elif(parsed_input[1] == "right"):
                        [move_status, move_description] = world.check_right(spaceplayer.x, spaceplayer.y)
                        print_wrap(move_description)
                        if(move_status):
                            spaceplayer.move_right()
                    elif(parsed_input[1] == "left"):
                        [move_status, move_description] = world.check_left(spaceplayer.x, spaceplayer.y)
                        print_wrap(move_description)
                        if(move_status):
                            spaceplayer.move_left()
                    else:
                        print("I don't understand where you're trying to go.")
                        
                    if(move_status):
                        print_wrap(world.tile_at(spaceplayer.x, spaceplayer.y).intro_text())
        if(debug_mode):
            print()
            print("RAW USER COMMAND: " + raw_input)
            print("PARSED USER COMMAND: " + str(parsed_input))
            
        world.updateRooms(spaceplayer)
                        
# These functions exist only to help make the text print nicer in the terminal.		
def get_width():
	dimensions = get_terminal_size()
	global wrap_width 
	if(dimensions[0] >= 20):
		wrap_width = dimensions[0] - 5		# Get the width of the user's window so we can wrap text.
	else:
		wrap_width = dimensions[0]						
	return dimensions
    
	
def clear_screen():
	terminal = get_width()
   
	for i in range(terminal[1]):
		print("")			# There are fancier ways to clear a screen, but this aligns our text where we want it at the bottom of the window.

		
def print_wrap(text):
	get_width()
	text = dedent(text)
	print(fill(text, wrap_width))
    

play()