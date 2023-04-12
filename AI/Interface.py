# On Créer une Interface Pour intéragir avec l'IA
# On utilise pygame pour créer une interface graphique

import pygame

# On crée une fonction pour initialiser l'interface
def InitInterface():
    pygame.init()
    pygame.display.set_caption("Deep Chess")
    screen = pygame.display.set_mode((1920, 1080))
    # On place un background
    background = pygame.image.load("../Data/Background/Background.png")
    screen.blit(background, (0, 0))


    # On charge l'image pour un bouton
    button = pygame.image.load("../Data/Noeuds.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (230, 49))
    # On affiche le bouton
    screen.blit(button, (845, 750))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Play.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (250, 50))
    # On affiche le bouton
    screen.blit(button, (835, 400))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Bots.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (200, 50))
    # On affiche le bouton
    screen.blit(button, (860, 470))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Test.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (190, 50))
    # On affiche le bouton
    screen.blit(button, (865, 540))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Database.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (215, 50))
    # On affiche le bouton
    screen.blit(button, (852, 610))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Train.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (215, 50))
    # On affiche le bouton
    screen.blit(button, (852, 680))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Credits.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (115, 50))
    # On affiche le bouton
    screen.blit(button, (1800, 960))

    # On affiche le Bouton pour jouer contre l'ia
    button = pygame.image.load("../Data/Quit.png")
    # On redimensionne l'image
    button = pygame.transform.scale(button, (115, 50))
    # On affiche le bouton
    screen.blit(button, (1800, 1020))


    return screen

# On créer une boucle pour pygame
def pygame_loop(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

        # On va détecter si le bouton est cliqué
        if pygame.mouse.get_pressed()[0]:
            # On récupère la position de la souris
            pos = pygame.mouse.get_pos()
            # On vérifie si la souris est dans le bouton
            if 850 < pos[0] < 1084 and 1000 < pos[1] < 1049:
                # On affiche un message
                print("Bouton cliqué")

        # On regarder si le bouton quitte est cliqué
        if pygame.mouse.get_pressed()[0]:
            # On récupère la position de la souris
            pos = pygame.mouse.get_pos()
            # On vérifie si la souris est dans le bouton
            if 1800 < pos[0] < 1915 and 1020 < pos[1] < 1070:
                # On affiche un message
                print("Bouton cliqué")
                # On quitte le programme
                pygame.quit()
                exit()

    pygame.quit()

# On lance l'interface dans le main
if __name__ == '__main__':
    screen = InitInterface()
    pygame_loop(screen)