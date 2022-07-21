'''DOCSTRING'''


class Board:
    '''DOCSTRING'''
    board = [[None, None, None],[None, None, None],[None, None, None]]

    def __init__(self):
        pass

    def __str__(self):
        string = ""
        seperator = "-------------------"
        for rows in self.board:
            single_row = " " + str(rows[0]) + " | " + str(rows[1]) + " | " + str(rows[1]) + "\n"
            string += single_row
        
        string.insert(seperator + "\n")

        string.removesuffix(seperator)
        return string


    def make_move(self, move):
        '''DOCSTRING'''

    def check_move(self):
        '''DOCSTRING'''


class Player:
    '''DOCSTRING'''
    def __init__(self, name, side):
        self.name = name
        self.side = side


def assign_player():
    '''DOCTSTRING'''


def initialise():
    '''DOCSTRING'''
    game_board = Board()
    return game_board


def main():
    '''DOCSTRING'''
    game_board = initialise()
    print(game_board)
    


if __name__ == '__main__':
    main()
