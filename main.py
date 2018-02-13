from spaceplayer import SpacePlayer
import shipmap

def play():
    print("Escape from USS Callister!")
    spaceplayer = SpacePlayer()
    while True:
        room = shipmap.tile_at(spaceplayer.x,spaceplayer.y)
        print(room.intro_text())
        action_input = get_spaceplayer_command()
        if action_input in ['f', 'F']:
            spaceplayer.move_forward()
        elif action_input in ['b', 'B']:
            spaceplayer.move_back()
        elif action_input in ['r', 'R']:
            spaceplayer.move_right()
        elif action_input in ['l', 'L']:
            spaceplayer.move_left()
        elif action_input in ['i', 'I']:
            spaceplayer.print_inventory()
        elif action_input in ['exit', 'Exit']:
            break
        else:
            print('Invalid Action!')
            
def get_spaceplayer_command():
    return input('Action: ')

play()