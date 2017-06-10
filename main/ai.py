import copy

class AI:
    """
    An AI that plays Tic Tac Toe perfectly using the Minimax algorithm
    """
    
    FIRST_MOVES = {(0, 1): (0, 0), (1, 2): (0, 2), (0, 0): (1, 1), (2, 0): (1, 1), (1, 0): 
                   (0, 0), (2, 2): (1, 1), (0, 2): (1, 1), (2, 1): (0, 1), (1, 1): (0, 0)}
    
    def __init__(self, player):
        self.player = player
        self.choice = None
    
    def get_score(self, game):
        if game.get_winner() == self.player:
            return 1
        elif game.get_winner() == self.get_other_figure(self.player):
            return -1
        return 0
        
    def get_other_figure(self, player):
        return 'X' if player == 'O' else 'O'
    
    def find_best_move(self, game):
        if game.get_player() != self.player:
            raise ValueError('find_best_move while it is not the turn of the AI')
        if game.field_empty():
            return (1, 1)
        elif len(game.get_possible_moves()) == 8:
            return AI.FIRST_MOVES[game.get_first_used_field()]
        
        self.minimax(game, -float('inf'), float('inf'))
        return choice
    
    def minimax(self, game, alpha, beta):
        global choice
        
        if game.get_winner() != 'NoWinner': return self.get_score(game)
        scores = []
        moves = []
        max_player = game.player == self.player
        for move in game.get_possible_moves():
            new_game = copy.deepcopy(game)
            new_game.set_figure(move)
            score = self.minimax(new_game, alpha, beta)
            
            if max_player and score > beta:
                return score
            if not max_player and score < alpha:
                return score
            
            if max_player and score > alpha: alpha = score
            if not max_player and score < beta: beta = score
            
            scores.append(score)
            moves.append(move)
            
            if max_player and score == 1: break
            elif not max_player and score == -1: break
        
        if max_player:
            max_score = max(scores)
            choice = moves[scores.index(max_score)]
            return max_score
        else:
            min_score = min(scores)
            choice = moves[scores.index(min_score)]
            return min_score
