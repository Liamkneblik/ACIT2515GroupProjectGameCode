from maze import Maze

new_maze = Maze('x.txt')

new_maze.display

print(new_maze.can_move_to(1,19))

print(new_maze.find_random_spot())

# y range0 - 11
# x  range0 - 19 