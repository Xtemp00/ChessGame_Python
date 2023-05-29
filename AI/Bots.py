# Code pour faire Jouer l'ia Contre un Bot avec un élo spécifique
# On va donc entrainer l'ia pour apprendre contre un bot et etudier sont comportement

import chess.engine
import chess
import pygame
import chess.engine

def InitInterface():
    pygame.init()
    pygame.display.set_caption("Chess")
    screen = pygame.display.set_mode((1920, 1080))

    # On affiche un background
    background = pygame.image.load("../Data/Background/Background Play.jpg")
    screen.blit(background, (0, 0))

    # On créé un bouton pour quitter
    button = pygame.image.load("../Data/Quit.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (115, 50))
    # On affiche le bouton
    screen.blit(button, (1800, 1020))



    return screen

def DrawBoard(screen):
    DrawAction(screen)

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (238, 238, 210), (i * 120, j * 120, 120, 120))
            else:
                pygame.draw.rect(screen, (118, 150, 86), (i * 120, j * 120, 120, 120))

# On fait une pop up pour le changement de pièces
def DrawPopUp(screen):
    # On affiche le cadre pour la promotion
    cadre = pygame.image.load("../Data/Background/Promotion.png")
    # On redimensionne l'image
    cadre = pygame.transform.scale(cadre, (700, 430))
    screen.blit(cadre, (125, 0))
    # On affiche les pièces possible pour la promotion
    # On affiche le bouton pour la tour
    button = pygame.image.load("../pieces/rook_white.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (125, 125))
    # On affiche le bouton
    screen.blit(button, (215, 225))
    # On affiche le bouton pour le fou
    button = pygame.image.load("../pieces/bishop_white.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (125, 125))
    # On affiche le bouton
    screen.blit(button, (340, 225))
    # On affiche le bouton pour le cavalier
    button = pygame.image.load("../pieces/knight_white.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (125, 125))
    # On affiche le bouton
    screen.blit(button, (465, 225))
    # On affiche le bouton pour la reine
    button = pygame.image.load("../pieces/queen_white.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (125, 125))
    # On affiche le bouton
    screen.blit(button, (590, 225))

    # On met un texte pour dire de choisir une pièce
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Promotion", True, (255, 255, 255))
    screen.blit(text, (375, 180))

    pygame.display.flip()


def CoupJoueAffichage(screen, liste_coup):

   # On affiche tout les coups de la liste
    for i in range(len(liste_coup)):
        # On affiche le coup
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render(str(liste_coup[i]), True, (255, 255, 255))
        screen.blit(text, (1140, 50 + i * 40))

    pygame.display.flip()

# On affiche certaine action
def DrawAction(screen):
    # On affiche un cadre
    cadre = pygame.image.load("../Data/Background/Cadre.png")
    # On redimensionne l'image
    cadre = pygame.transform.scale(cadre, (400, 960))
    # On affiche le bouton
    screen.blit(cadre, (900, 15))


def DrawPieces(screen, board):
    pieces = {'P': pygame.image.load('../pieces/pawn_white.png'), 'N': pygame.image.load('../pieces/knight_white.png'), 'B': pygame.image.load('../pieces/bishop_white.png'), 'R': pygame.image.load('../pieces/rook_white.png'), 'Q': pygame.image.load('../pieces/queen_white.png'), 'K': pygame.image.load('../pieces/king_white.png')
              , 'p': pygame.image.load('../pieces/pawn_black.png'), 'n': pygame.image.load('../pieces/knight_black.png'), 'b': pygame.image.load('../pieces/bishop_black.png'), 'r': pygame.image.load('../pieces/rook_black.png'), 'q': pygame.image.load('../pieces/queen_black.png'), 'k': pygame.image.load('../pieces/king_black.png')}
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i, j))
            if piece is not None:
                # On redimensionne la pièce
                pieces[piece.symbol()] = pygame.transform.scale(pieces[piece.symbol()], (120, 120))
                # On affiche la pièce blanche en bas et les noirs en haut
                screen.blit(pieces[piece.symbol()], (i * 120, (7 - j) * 120))



# On fait une fonction pour faire un Highlight sur la case sélectionnée
def highlight_square(screen, square, board):
    # On récupère le type de pièce sélectionnée
    piece = board.piece_at(square)

    # On affiche un cercle vert transparent sur la case sélectionnée
    surface = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.circle(surface, (192, 192, 192, 150), (30, 30), 40)
    screen.blit(surface, (chess.square_file(square) * 120+30, (7 - chess.square_rank(square)) * 120+30))
    pygame.display.flip()
    # On regarde les coups possibles de la pièce sélectionnée
    moves = board.legal_moves

    # On affiche un carre vert transparent sur les case possible
    for move in moves:
        if move.from_square == square:
            surface = pygame.Surface((60, 60), pygame.SRCALPHA)
            pygame.draw.circle(surface, (192, 192, 192, 150), (30, 30), 30)
            screen.blit(surface, (chess.square_file(move.to_square) * 120+30, (7 - chess.square_rank(move.to_square)) * 120+30))
            pygame.display.flip()


# On vérifie l''état de la partie si il y a échec ou pas
def check_game_state(board):
    if board.is_checkmate():
        print("Echec et mat")
        return True
    elif board.is_stalemate():
        print("Pat")
        return True
    elif board.is_insufficient_material():
        print("Insuffisance de matériel")
        return True
    elif board.is_seventyfive_moves():
        print("75 coups sans prise")
        return True
    elif board.is_fivefold_repetition():
        print("5 répétitions")
        return True
    else:
        return False

# On affiche un texte en jeu pour dire que la partie est terminé
def draw_text(screen, text):
    font = pygame.font.SysFont('Arial', 40)
    text = font.render(text, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (400, 400)
    screen.blit(text, text_rect)


# On lance la boucle de Jeu
def game_loop():
    screen = InitInterface()
    engine = chess.engine.SimpleEngine.popen_uci("StockFish/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")
    elo = 0
    #On définie un niveau pour le moteur
    engine.configure({"Skill Level": elo})
    board = chess.Board()
    DrawBoard(screen)
    DrawPieces(screen, board)
    pygame.display.flip()
    #DrawPopUp(screen)
    tour = 0

    coup_joue =[]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if check_game_state(board):
            draw_text(screen, "Partie Terminé")
            pygame.display.flip()
            pygame.quit()
            exit()

        # On regarde si le bouton quit est cliqué
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            # On regarde si la souris est sur le bouton
            if 1800 < pos[0] < 1915 and 1020 < pos[1] < 1070:
                pygame.quit()
                exit()

        # On regarde si une pièce est sélectionnée
        if pygame.mouse.get_pressed()[0] and tour == 0 and pygame.mouse.get_pos()[0] < 960 and pygame.mouse.get_pos()[1] < 960:
            # On récupère la position de la souris
            pos = pygame.mouse.get_pos()
            # On récupère la case correspondante, on tien compte du décalage de 220 et 200
            square = (pos[0]// 120 , pos[1] // 120)
            print(square)
            # On récupère la pièce présente sur cette case
            piece = board.piece_at(chess.square(square[0], 7 - square[1]))
            # On regarde que la pièce est bien de la couleur du joueur cette a dire blanche
            if piece is not None and piece.color == chess.WHITE:
                # On affiche la pièce sélectionnée et sa position
                print(piece.symbol(), square)
                # On a la position initial de la pièce
                initial_square = square
                # On affiche un carré vert sur la case sélectionnée
                highlight_square(screen, chess.square(square[0], 7 - square[1]), board)
                # On récupère la position final de la pièce
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        square = (pos[0] // 120 , pos[1] // 120)
                        # On regarde que la case est bien différente de la case initiale
                        if square != initial_square:
                            # On regarde que la case est bien vide
                            # Déplacement de la pièce
                            colonne = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                            move = str(colonne[initial_square[0]]) + str(8 - initial_square[1]) + str(
                                colonne[square[0]]) + str(8 - square[1])
                            move = chess.Move.from_uci(move)
                            if move in board.legal_moves:
                                board.push(move)
                                print(board)
                                DrawBoard(screen)
                                DrawPieces(screen, board)
                                coup_joue.append(move)
                                CoupJoueAffichage(screen, coup_joue)
                                pygame.display.flip()
                                tour = 1
                                break
                    # Si le clique droit est pressé on annule le déplacement et on déselectionne la pièce
                    if pygame.mouse.get_pressed()[2]:
                        DrawBoard(screen)
                        DrawPieces(screen, board)
                        pygame.display.flip()
                        break

        elif tour == 1:
            print("C'est au tour du bot")
            # C'est au tour du bot
            result = engine.play(board, chess.engine.Limit(time=1.0))
            board.push(result.move)
            DrawBoard(screen)
            DrawPieces(screen, board)
            coup_joue.append(result.move)
            CoupJoueAffichage(screen, coup_joue)
            pygame.display.flip()
            tour = 0


# On lance l'interface dans le main
if __name__ == '__main__':
    game_loop()