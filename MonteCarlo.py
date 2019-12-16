import OthelloEngine.py
import random
from collections import Counter

class MonteCarloAI:
    
    #game = GameEngine(white_team_file, black_team_file, output_file)
    
    def __init__(self, color, n, time_limit):
        self.team_type = color
        self.opponentColor = 'W' if color == 'B' else 'B'
    
    def get_team_name(self):
        return "team Team"
    
    def randMove(self, board):
        
        for move in possibleMoves:
            coordinates = move[1]
            possibleMoves.append(coordinates)
        randomMove = random.choice(possibleMoves)
        return randomMove


    def get_move(self, board):
        counter = Counter()
        
        possibleMoves = OthelloEngine.get_all_moves(board, self.color)
        coordinates = []
        for move in possibleMoves:
            coordinates.append(move[1])
        randomMove = random.choice(coordinates)
        for moves in randomMove:
            for i in range(100):
                tempBoard = deepcopy(board)
                #game.update_board(moves)
                if winner == self.color:
                    counter[moves] += 1
        nextMove = counter.most_common(1)[0][0] if len(counter) > 0 else random.choice(moves)
        return nextMove
