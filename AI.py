import pygame
from time import sleep
from Game import Game

class AI:  # Classe qui permet de créer un IA
    def __init__(self):
        # On va récupérer le plateau d'échec sous forme de tableau
        game = Game()  # On récupère le jeu
        self.grid = game.get_grid()  # On récupère le plateau de jeu
        self.Affichage_type()  # On affiche le tableau

    def Affichage_type(self):  # Affichage du tableau
        AI_grid = [[0 for i in range(8)] for j in range(8)]  # Création d'un tableau de 8*8
        for i in range(8):  # On parcours le tableau
            for j in range(8):  # On parcours le tableau
                if self.grid[i][j] is not None:  # Si la case n'est pas vide
                    AI_grid[i][j] = [self.grid[i][j].get_type(), self.grid[i][j].get_color(), i,
                                     j]  # On ajoute le type de la pièce
                else:  # Sinon
                    AI_grid[i][j] = ["None", i, j]  # On ajoute "None"
            print("")  # On saute une ligne
        print(AI_grid)  # On affiche le tableau

    def Input(self, x, y):
        # Coordoner de d'arriver x,y
        self.x = x
        self.y = y
        game = Game()  # On récupère le plateau de jeu
        self.grid = game.get_grid()  # On récupère le plateau de jeu
        for i in range(8):  # On parcours le tableau
            for j in range(8):  # On parcours le tableau
                if self.grid[x][y] is not None:  # Si la case n'est pas vide
                    # Déplacement de la pièces a la position final
                    game.set_grid(self.grid)  # On place le plateau de jeu

    def get_grid(self):  # Fonction qui permet de récupérer le plateau de jeu
        return self.grid  # On retourne le plateau de jeu

    def set_grid(self, grid):  # Fonction qui permet de placer le plateau de jeu
        self.grid = grid  # On place le plateau de jeu

    def get_AI_grid(self):  # Fonction qui permet de récupérer le plateau de jeu
        return self.AI_grid  # On retourne le plateau de jeu

    def set_AI_grid(self, AI_grid):  # Fonction qui permet de placer le plateau de jeu
        self.AI_grid = AI_grid  # On place le plateau de jeu

