"""
Class responsible for storing all information about current state of a chess game. Will also be responsible for
determining the valid moves at the current state, will also keep a move log
"""

#can use numpy arrays for more efficiency
class GameState():
    def __init__(self):
        #board is an 8x8 2d list, each element of the list has 2 characters
        #first character represents the color, second character is type of piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []