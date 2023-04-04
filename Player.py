import pygame  # Importation de la bibliothèque pygame

class Player:  # Classe qui permet de créer un joueur

    def __init__(self, color, turn):  # Méthode d'initialisation de la classe
        self.color = color  # Couleur du joueur
        self.pieces = []  # Liste des pièces du joueur
        self.turn = turn  # Tour du joueur

    def get_color(self):  # Fonction qui permet de récupérer la couleur du joueur
        return self.color  # On retourne la couleur du joueur

    def get_pieces(self):  # Fonction qui permet de récupérer les pièces du joueur
        return self.pieces  # On retourne les pièces du joueur

    def set_color(self, color):  # Fonction qui permet de changer la couleur du joueur
        self.color = color  # On change la couleur du joueur

    def set_pieces(self, pieces):  # Fonction qui permet de changer les pièces du joueur
        self.pieces = pieces  # On change les pièces du joueur

    def get_turn(self):  # Fonction qui permet de récupérer le tour du joueur
        return self.turn  # On retourne le tour du joueur

    def set_turn(self, turn):  # Fonction qui permet de changer le tour du joueur
        self.turn = turn  # On change le tour du joueur
