class Game(object):
    def __init__(self, start_player):
        self.player = start_player
        self.start_player = start_player
        self.field = {(0, 0): None, (0, 1): None, (0, 2): None,
                      (1, 0): None, (1, 1): None, (1, 2): None,
                      (2, 0): None, (2, 1): None, (2, 2): None}
        self.winning_vectors = [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
        ]
        self.move_count = 0

    def set_figure(self, pos):
        if self.field[pos] != None:
            raise ValueError('Field is already used')
        self.field[pos] = self.player
        self.change_player()
        self.move_count += 1

    def change_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def get_player(self):
        return self.player

    def get_winner(self):
        for vector in self.winning_vectors:
            if self.same_figure_everywhere(vector):
                return self.field[vector[0]]

        if self.field_full():
            return 'Tie'

        return 'NoWinner'

    def same_figure_everywhere(self, vector):
        figure = self.field[vector[0]]
        if figure is None: return False
        for f in vector:
            if figure != self.field[f]: return False
        return True

    def field_full(self):
        return len([v for v in self.field.values() if v is not None]) == 9

    def field_empty(self):
        return len([v for v in self.field.values() if v is not None]) == 0

    def get_first_used_field(self):
        for pos in self.field:
            if self.field[pos] != None: return pos

    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.field[(i, j)] == None: moves.append((i, j))
        return moves

    def restart(self):
        other = 'O' if self.start_player == 'X' else 'X'
        self.__init__(other)
