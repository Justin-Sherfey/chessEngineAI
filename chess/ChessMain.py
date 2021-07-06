"""
Main driver file, responsible for handling user input and displaying current GameState object
"""
import pygame as p
from chess import ChessEngine

# global variables
WIDTH = HEIGHT = 512
DIMENSION = 8  # dimension of chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations
IMAGES = {}

'''
Initialize global dictionary of images. This will be called exactly once in main
'''


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess_pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # can now access piece by using 'IMAGES['wp']


'''
main driver for code, will handle user input and updating graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()  # only do this once before while loop
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


'''
Responsible for all graphics within a current game state
'''


def drawGameState(screen, gs):
    draw_board(screen)  # draws squares on board
    draw_pieces(screen, gs.board)


'''
Draws squares on board, top left square is always light
'''


def draw_board(screen):
    colors = [p.Color("white"), p.color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draws the pieces on the board using the current gamestate.board
'''


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r, c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
