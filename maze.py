import random

class Maze:
    def __init__(self,filename):
        '''
        Scans the maze file and puts it into list,
        while also saving the maze dimensions into lines and cols
        '''
        _content = []
        self._cols = 0
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                _content.append(line.strip('\n'))
                self._cols = len(line) - 1
        self._lines = len(_content) - 1 
        self._maze = _content
        self.item1 = self.find_random_spot()
        self.item2 = self.find_random_spot()
        self.item3 = self.find_random_spot()
        self.item4 = self.find_random_spot()


    def is_item(self):
        '''
        Supposed to check if current location is an item
        '''
        pass

    def can_move_to(self,line_number,column_number):
        '''
        Checks if coordinate inputed is a wall ,if not the it will return True
        '''
        if self._maze[line_number][column_number] == 'X':
            return False
        else:
            return True 
    @property
    def display(self):
        for line in self._maze:
            print(line)

    def find_random_spot(self):
        """
        Looks for a random spot in the maze, and will return the coordinates
        """
        empty_space = False
        while empty_space != True:
            line_num = random.randint(0,self._lines)
            col_num = random.randint(0,self._cols)
            if (self.can_move_to(line_num,col_num) == True):
                empty_space = True
                return line_num , col_num
