import tensorflow as tf
from keras.utils.vis_utils import plot_model
import netron



def AfficherGraphique(model):
    # Visualiser le graphique de votre modèle avec netron
    # Visualiser le graphique de votre modèle avec Netron
    netron.start(model)