from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# the directions for backtracking
rev_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# My code
'''  Trying to understand:
- find what room a player is currently in
- maybe use the player methods in the search
- use get_exits from room def
Helpful methods
player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)
    
vertex = current rooms
edges = paths directions
# Depth-first traversal following hint
'''


# BFS(breadth_first_search) to search the paths through the maze

# Fill this out with directions to walk
traversal_path = []

# A dictionary of checked rooms
mapDic = {}


def breadth_first_search(starting_room_id):
    q = Queue()
    q.enqueue([starting_room_id])
    visited = set()

    while q.size() > 0:
        # first path
        path = q.dequeue()
        # taking last path
        current_room = path[-1]
        visited.add(current_room)
        # each direction in the map graphs current_room
        for direction in mapDic[current_room]:
            if mapDic[current_room][direction] == '?':
                return path
            elif mapDic[current_room][direction] not in visited:
                # create a new path that is added to direction dictionary
                new_path = list(path)
                new_path.append(mapDic[current_room][direction])
                q.enqueue(new_path)


while len(mapDic) != len(room_graph):
    # the room the player is in
    current_room = player.current_room
    # the rooms id
    room_id = current_room.id
    current_room_dic = {}  # current_room_dictonary

    # Check to see if player has explored the room already
    if room_id not in mapDic:
        # Record exits and add key as '?'
        for i in current_room.get_exits():
            current_room_dic[i] = '?'
        # Update with previous room id
        if traversal_path:
            # prev room is the oppsite of the last travel path
            prev_dir = rev_dir[traversal_path[-1]]
            current_room_dic[prev_dir] = visted_room_id
        # Update room dictonary with the unexplored exit
        mapDic[room_id] = current_room_dic
    # If it already visted, grab data from outer dictionary using room_id
    else:
        current_room_dic = mapDic[room_id]

    # Check to see if there are still unvisted rooms connected
    # storing the exits ('?')
    unexplored_exits = list()
    # loop through the room dictionary
    for direction in current_room_dic:
        if current_room_dic[direction] == '?':
            unexplored_exits.append(direction)  # storing exists based on the ?

    # If unexplored exist, go in that the directions
    if len(unexplored_exits) != 0:
        direction = unexplored_exits[0]
        traversal_path.append(direction)
        player.travel(direction)
        # Update the exists
        room_move = player.current_room
        mapDic[current_room.id][direction] = room_move.id
        visted_room_id = current_room.id
    # Otherwise, find a way back to closest room with an unknown exit
    else:
        # Find closest room using the breadth_first_search
        path_to_next = breadth_first_search(room_id)

        # check that data is returned from bfs
        if path_to_next is not None and len(path_to_next) > 0:
            # Have the player travel back to room with unknown exits
            # iterate the length of the dictionary
            for i in range(len(path_to_next) - 1):
                # lopp the through the mapDic to find the direction
                for direction in mapDic[path_to_next[i]]:
                    # if mapDic path to next room  and direction matches the room index found in the bfs
                    if mapDic[path_to_next[i]][direction] == path_to_next[i + 1]:
                        traversal_path.append(direction)
                        # player likes to move it move it to that room
                        player.travel(direction)
        else:
            break  # the end is here!


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
